import random
from typing import List

from eckity.genetic_encodings.ga.vector_individual import Vector
from eckity.genetic_operators.genetic_operator import GeneticOperator


class VectorUniformCrossover(GeneticOperator):
    def __init__(self, probability=1, events=None):
        """
        Vector uniform crossover
        Given 2 vectors for every corresponding elements (same index)
        preform a switch in values based on given probability.

        Parameters
        ----------
        probability : float
            The probability of the crossover operator to be applied to each vector element

        events: list of strings
            Events to publish before/after the mutation operator
        """
        self.individuals = None
        self.applied_individuals = None
        super().__init__(probability=probability, arity=2, events=events)

    def apply(self, individuals: List[Vector]) -> List[Vector]:
        """
        Attempt to perform the crossover operator

        Parameters
        ----------
        individuals : list of individuals to perform crossover on

        Returns
        ----------
        list of individuals
        individuals after the crossover
        """
        self.individuals = individuals
        size = len(individuals[0].vector)

        for i in range(size):
            if random.random() < self.probability:
                val1 = individuals[0].cell_value(i)
                val2 = individuals[1].cell_value(i)
                individuals[0].set_cell_value(i, val2)
                individuals[1].set_cell_value(i, val1)

        self.applied_individuals = individuals
        return individuals


class FloatVectorBlendCrossover(GeneticOperator):
    def __init__(self, probability=1, alpha=0.5, events=None):
        """
        Float Vector Blend crossover
        Given 2 vectors for every corresponding elements (same index)
        preform a blend in values based on

        Parameters
        ----------
        probability : float
            The probability of the crossover operator to be applied to each vector element

        alpha: float
            For each element on both side of the parents’ determent
            the extent of the interval in which the new values can be drawn

        events: list of strings
            Events to publish before/after the mutation operator
        """
        self.individuals = None
        self.applied_individuals = None
        self.alpha = alpha
        super().__init__(probability=probability, arity=2, events=events)

    def apply(self, individuals: List[Vector]) -> List[Vector]:
        """
        Attempt to perform the crossover operator

        Parameters
        ----------
        individuals : list of individuals to perform crossover on

        Returns
        ----------
        list of individuals
        individuals after the crossover
        """
        self.individuals = individuals
        size = len(individuals[0].vector)

        for i in range(size):
            if random.random() < self.probability:
                blend_ratio = random.uniform(0, self.alpha)

                old_val1 = individuals[0].cell_value(i)
                old_val2 = individuals[1].cell_value(i)
                new_val1 = (1.0 - blend_ratio) * old_val1 + blend_ratio * old_val2
                new_val2 = blend_ratio * old_val1 + (1.0 - blend_ratio) * old_val2

                individuals[0].set_cell_value(i, new_val1)
                individuals[1].set_cell_value(i, new_val2)

        self.applied_individuals = individuals
        return individuals
