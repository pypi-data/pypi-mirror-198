from typing import TYPE_CHECKING, Dict, Optional


from unified_planning.shortcuts import (
    UserType,
    Object,
    BoolType,
    IntType,
    Fluent,
    InstantaneousAction,
    Problem,
    Or,
    And,
    GE,
    LE,
    OneshotPlanner,
)
from unified_planning.plans import SequentialPlan
from unified_planning.engines.results import PlanGenerationResult

from hcraft.transformation import Transformation, InventoryOwner
from hcraft.task import Task, GetItemTask, PlaceItemTask, GoToZoneTask
from hcraft.purpose import Purpose
from hcraft.elements import Zone, Item

if TYPE_CHECKING:
    from hcraft.state import HcraftState


class HcraftPlanningProblem:
    """Interface between the unified planning framework and HierarchyCraft."""

    def __init__(
        self, state: "HcraftState", name: str, purpose: Optional["Purpose"]
    ) -> None:
        """Initialize a HierarchyCraft planning problem on the given state and purpose.

        Args:
            state: Initial state of the HierarchyCraft environment.
            name: Name of the planning problem.
            purpose: Purpose used to compute the planning goal.
        """
        self.upf_problem: Optional[Problem] = self._init_problem(state, name, purpose)
        self.plan: Optional[SequentialPlan] = None

    def action_from_plan(self, state: "HcraftState") -> int:
        """Get the next gym action from a given state.

        If a plan is already existing, just use the next action in the plan.
        If no plan exists, first update and solve the planning problem.

        Args:
            state (HcraftState): Current state of the hcraft environement.

        Returns:
            int: Action to take according to the plan.
        """
        if self.plan is None:
            self.update_problem_to_state(state)
            self.solve()
        plan_action_name = str(self.plan.actions.pop(0))
        if not self.plan.actions:
            self.plan = None
        action = int(plan_action_name.split("_")[0])
        return action

    def update_problem_to_state(self, state: "HcraftState"):
        """Update the planning problem initial state to the given state.

        Args:
            state: HierarchyCraft state to use as reference for the
                initial state of the planning problem.
        """
        current_pos = state.current_zone
        for zone in state.world.zones:
            discovered = state.has_discovered(zone)
            if current_pos is not None:
                self.upf_problem.set_initial_value(
                    self.pos(self.zones_obj[zone]), zone == current_pos
                )
            self.upf_problem.set_initial_value(
                self.visited(self.zones_obj[zone]), discovered
            )

        for item in state.world.items:
            quantity = state.amount_of(item)
            self.upf_problem.set_initial_value(
                self.amount(self.items_obj[item]), quantity
            )

        for zone in state.world.zones:
            for zone_item in state.world.zones_items:
                quantity = state.amount_of(zone_item, zone)
                self.upf_problem.set_initial_value(
                    self.amount_at(
                        self.zone_items_obj[zone_item], self.zones_obj[zone]
                    ),
                    quantity,
                )

    def solve(self) -> PlanGenerationResult:
        """Solve the current planning problem with a planner."""
        with OneshotPlanner(problem_kind=self.upf_problem.kind) as planner:
            results = planner.solve(self.upf_problem)
        self.plan = results.plan
        return results

    def _init_problem(
        self, state: "HcraftState", name: str, purpose: Optional["Purpose"]
    ) -> Problem:
        """Build a unified planning problem from the given world and purpose.

        Args:
            world: HierarchyCraft world to generate the problem from.
            name: Name given to the planning problem.
            purpose: Purpose of the agent.
                Will be used to set the goal of the planning problem.

        Returns:
            Problem: Unified planning problem.
        """
        self.upf_problem = Problem(name)
        self.zone_type = UserType("zone")
        self.player_item_type = UserType("player_item")
        self.zone_item_type = UserType("zone_item")

        self.zones_obj: Dict[Zone, Object] = {}
        for zone in state.world.zones:
            self.zones_obj[zone] = Object(zone.name, self.zone_type)

        self.items_obj: Dict[Item, Object] = {}
        for item in state.world.items:
            self.items_obj[item] = Object(item.name, self.player_item_type)

        self.zone_items_obj: Dict[Item, Object] = {}
        for item in state.world.zones_items:
            self.zone_items_obj[item] = Object(
                f"{item.name}_in_zone", self.zone_item_type
            )

        self.upf_problem.add_objects(self.zones_obj.values())
        self.upf_problem.add_objects(self.items_obj.values())
        self.upf_problem.add_objects(self.zone_items_obj.values())

        self.pos = Fluent("pos", BoolType(), zone=self.zone_type)
        self.visited = Fluent("visited", BoolType(), zone=self.zone_type)
        self.amount = Fluent("amount", IntType(), item=self.player_item_type)
        self.amount_at = Fluent(
            "amount_at", IntType(), item=self.zone_item_type, zone=self.zone_type
        )

        self.upf_problem.add_fluent(self.pos, default_initial_value=False)
        self.upf_problem.add_fluent(self.visited, default_initial_value=False)
        self.upf_problem.add_fluent(self.amount, default_initial_value=0)
        self.upf_problem.add_fluent(self.amount_at, default_initial_value=0)

        actions = []
        for t_id, transfo in enumerate(state.world.transformations):
            actions.append(self._action_from_transformation(transfo, t_id))

        self.upf_problem.add_actions(actions)

        if purpose is not None and purpose.terminal_groups:
            self.upf_problem.add_goal(self._purpose_to_goal(purpose))

        self.update_problem_to_state(state)
        return self.upf_problem

    def _action_from_transformation(
        self, transformation: "Transformation", transformation_id: int
    ) -> InstantaneousAction:
        action_name = f"{transformation_id}_{transformation.name}"
        action = InstantaneousAction(action_name)
        loc = None
        if len(self.zones_obj) > 0:
            action = InstantaneousAction(action_name, loc=self.zone_type)
            loc = action.parameter("loc")
            action.add_precondition(self.pos(loc))

        if transformation.zones and len(self.zones_obj) > 1:
            action.add_precondition(
                Or(*[self.pos(self.zones_obj[zone]) for zone in transformation.zones])
            )

        if transformation.destination is not None:
            action.add_effect(self.pos(loc), False)
            action.add_effect(
                self.visited(self.zones_obj[transformation.destination]), True
            )
            action.add_effect(
                self.pos(self.zones_obj[transformation.destination]), True
            )

        self._add_player_operation(action, transformation)
        self._add_current_zone_operations(action, transformation, loc)
        return action

    def _add_player_operation(
        self,
        action: InstantaneousAction,
        transfo: Transformation,
    ):
        player = InventoryOwner.PLAYER
        add_item_to_quantity = {}
        for stack in transfo.get_changes(player, "add", []):
            stack_amount = self.amount(self.items_obj[stack.item])
            action.add_increase_effect(stack_amount, stack.quantity)
            add_item_to_quantity[stack.item] = stack.quantity

        for stack in transfo.get_changes(player, "remove", []):
            stack_amount = self.amount(self.items_obj[stack.item])
            action.add_precondition(GE(stack_amount, stack.quantity))
            action.add_decrease_effect(stack_amount, stack.quantity)

        for max_stack in transfo.get_changes(player, "max", []):
            stack_amount = self.amount(self.items_obj[max_stack.item])
            removed = add_item_to_quantity.get(max_stack.item, 0)
            action.add_precondition(LE(stack_amount, max_stack.quantity - removed))

    def _add_current_zone_operations(
        self,
        action: InstantaneousAction,
        transfo: Transformation,
        loc,
    ):
        amount_at = self.upf_problem.fluent("amount_at")
        current = InventoryOwner.CURRENT
        add_item_to_quantity = {}
        for stack in transfo.get_changes(current, "add", []):
            amount_at_loc = amount_at(self.zone_items_obj[stack.item], loc)
            action.add_increase_effect(amount_at_loc, stack.quantity)
            add_item_to_quantity[stack.item] = stack.quantity

        for rem_stack in transfo.get_changes(current, "remove", []):
            amount_at_loc = amount_at(self.zone_items_obj[rem_stack.item], loc)
            action.add_precondition(GE(amount_at_loc, rem_stack.quantity))
            action.add_decrease_effect(amount_at_loc, rem_stack.quantity)

        for max_stack in transfo.get_changes(current, "max", []):
            amount_at_loc = amount_at(self.zone_items_obj[max_stack.item], loc)
            removed = add_item_to_quantity.get(max_stack.item, 0)
            action.add_precondition(LE(amount_at_loc, max_stack.quantity - removed))

    def _task_to_goal(self, task: "Task"):
        if isinstance(task, GetItemTask):
            item = self.items_obj[task.item_stack.item]
            return GE(self.amount(item), task.item_stack.quantity)
        if isinstance(task, PlaceItemTask):
            item = self.zone_items_obj[task.item_stack.item]
            zones = self.zones_obj.keys()
            if task.zones is not None:
                zones = [zone for zone in task.zones]
            conditions = [
                GE(self.amount_at(item, self.zones_obj[zone]), task.item_stack.quantity)
                for zone in zones
            ]
            return Or(*conditions)
        if isinstance(task, GoToZoneTask):
            return self.visited(self.zones_obj[task.zone.name])
        raise NotImplementedError

    def _purpose_to_goal(self, purpose: "Purpose"):
        # Individual tasks goals
        goals = {}
        for task in purpose.tasks:
            goals[task] = self._task_to_goal(task)

        # We only consider the best terminal group goal
        return And(*[goals[task] for task in purpose.best_terminal_group.tasks])
