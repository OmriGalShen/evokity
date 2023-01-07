from eckity.genetic_encodings.gp.tree.tree_individual import Tree
import pytest
from evokity.mutations import TreeShrinkMutation
from eckity.creators.gp_creators.ramped_hh import RampedHalfAndHalfCreator
from eckity.genetic_encodings.gp.tree.functions import (
    f_add,
    f_mul,
    f_sub,
    f_div,
    f_sqrt,
    f_log,
    f_abs,
    f_max,
    f_min,
    f_inv,
    f_neg,
)


@pytest.fixture
def individuals() -> list[Tree]:
    function_set = [
        f_add,
        f_mul,
        f_sub,
        f_div,
        f_sqrt,
        f_log,
        f_abs,
        f_max,
        f_min,
        f_inv,
        f_neg,
    ]
    terminal_set = ["x", "y", "z", 0, 1, -1]
    creator = RampedHalfAndHalfCreator(
        init_depth=(2, 2),
        terminal_set=terminal_set,
        function_set=function_set,
        bloat_weight=0.0001,
    )
    return creator.create_individuals(1, True)


def test_tree_shrink_basic(individuals):
    mutator = TreeShrinkMutation()
    mutated_individuals = mutator.apply(individuals)
    mutated = mutated_individuals[0]
    individial = individuals[0]
    assert mutated.tree != individial.tree
    assert len(mutated.tree) < len(individial.tree)


def test_tree_no_shrink(individuals):
    mutator = TreeShrinkMutation(probability=0)
    mutated_individuals = mutator.apply(individuals)
    mutated = mutated_individuals[0]
    individial = individuals[0]
    assert mutated.tree == individial.tree
