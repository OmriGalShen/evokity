import random
from copy import deepcopy
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
        individuals = deepcopy(individuals)
        self.individuals = individuals

        for i in range(len(individuals[0].vector)):
            if random.random() < self.probability:
                individuals[0].vector[i], individuals[1].vector[i] = (
                    individuals[1].vector[i],
                    individuals[0].vector[i],
                )

        self.applied_individuals = individuals
        return individuals
