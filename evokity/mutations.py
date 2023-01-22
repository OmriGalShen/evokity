import random
from copy import deepcopy
from typing import Optional

from eckity.genetic_encodings.gp.tree.tree_individual import Tree
from eckity.genetic_operators.genetic_operator import GeneticOperator
from eckity.genetic_operators.mutations.vector_n_point_mutation import (
    VectorNPointMutation,
)


class VectorShuffleIndexesNPointMutation(VectorNPointMutation):
    """
    Uniform N Point indexes shuffle mutation.
    """

    def __init__(self, probability=1.0, events=None, n=2):
        super().__init__(probability=probability, arity=1, events=events, n=n)

    def attempt_operator(self, individuals, attempt_num):
        """
        Attempt to perform the mutation operator
        Parameters
        ----------
        individuals : list of individuals to mutate
        attempt_num : int
            Current attempt number
        Returns
        ----------
        tuple of (bool, list of individuals)
            first return value determines if the attempt succeeded
            second return value is the operator result
        """
        succeeded = True

        for individual in individuals:
            selected_n_points_indexes = random.sample(
                range(individual.size()), k=self.n
            )
            for i in selected_n_points_indexes:
                if random.random() < self.probability:
                    selected_without_i = [
                        j for j in selected_n_points_indexes if j != i
                    ]
                    if len(selected_without_i) > 0:
                        swap_index = random.choice(selected_without_i)
                        swap_values(individual, i, swap_index)

        self.applied_individuals = individuals
        return succeeded, individuals


def swap_values(individual, i, swap_index):
    tmp = individual.cell_value(swap_index)
    individual.set_cell_value(swap_index, individual.cell_value(i))
    individual.set_cell_value(i, tmp)


class TreeShrinkMutation(GeneticOperator):
    def __init__(self, probability=1, max_iterations=100, arity=1, events=None):
        """
        This operator shrinks the *individual* by choosing randomly a branch and
        replacing it with one of the branch's arguments (also randomly chosen).
        """
        super().__init__(probability=probability, arity=arity, events=events)
        self.max_iterations = max_iterations

    def apply(self, individuals_: list[Tree]) -> list[Tree]:
        """
        Apply mutation in-place on `individuals`.
        Returns
        -------
        List of mutated individuals.
        """
        individuals = deepcopy(individuals_)
        for individual in individuals:
            copy = deepcopy(individual)
            if random.random() > self.probability:
                continue

            modified = False
            iteration = 0
            # while not modified and iteration < self.max_iterations:
            while not modified and iteration < self.max_iterations:
                # Convert subtree list to a `Tree` object, using deepcopy hackery.
                subtree = deepcopy(individual)
                subtree.tree = individual.random_subtree()
                sub_subtree = subtree.random_subtree()
                index = index_of_subtree(individual.tree, subtree.tree)
                assert index is not None
                replace_subtree(individual, index, sub_subtree)
                if individual.tree != copy.tree:
                    modified = True
                iteration += 1

        self.applied_individuals = individuals
        return individuals


def index_of_subtree(tree: list, subtree: list) -> Optional[int]:
    """
    Return the index of `subtree` in `tree`.
    """
    for i in range(len(tree)):
        if tree[i : i + len(subtree)] == subtree:
            return i
    return None


def replace_subtree(tree: Tree, index: int, new_subtree: list):
    """
    Replace the subtree starting at `index` with `new_subtree`

    Parameters
    ----------
    subtree - new subtree to replace some existing subtree in this individual's tree

    Returns
    -------
    None
    """
    end_i = tree._find_subtree_end([index])
    left_part = tree.tree[:index]
    right_part = tree.tree[(end_i + 1) :]
    tree.tree = left_part + new_subtree + right_part


class FloatVectorMultiplierNPointMutation(VectorNPointMutation):
    """
    N Point Float Vector Multiplier Mutation
    Randomly chooses N vector cells and multiply them with a random variable between given bounds

    Parameters
    ----------
    probability : float
        The probability of the crossover operator to be applied to each vector element

    left_bound : float
        The left (including) bound for the random multiplier used to change the value of chosen vector cell

    right_bound : float
        The right bound (including) for the random multiplier used to change the value of chosen vector cell

    events: list of strings
        Events to publish before/after the mutation operator
    """

    def __init__(
        self, probability=1.0, n=1, left_bound=0.0, right_bound=1.0, events=None
    ):
        super().__init__(probability=probability, arity=1, events=events, n=n)
        self.left_bound = left_bound
        self.right_bound = right_bound

    def attempt_operator(self, individuals, attempt_num):
        """
        Attempt to perform the mutation operator
        Parameters
        ----------
        individuals : list of individuals to mutate
        attempt_num : int
            Current attempt number
        Returns
        ----------
        tuple of (bool, list of individuals)
            first return value determines if the attempt succeeded
            second return value is the operator result
        """
        succeeded = True

        for individual in individuals:
            selected_n_points_indexes = random.sample(
                range(individual.size()), k=self.n
            )
            for i in selected_n_points_indexes:
                if random.random() < self.probability:
                    multiplier_factor = random.uniform(
                        self.left_bound, self.right_bound
                    )
                    value = individual.cell_value(i)
                    new_value = value * multiplier_factor
                    individual.set_cell_value(i, new_value)

        self.applied_individuals = individuals
        return succeeded, individuals
