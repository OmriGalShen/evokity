import random
from eckity.evaluators.simple_population_evaluator import Individual
from eckity.genetic_operators.mutations.vector_n_point_mutation import (
    VectorNPointMutation,
)


class VectorShuffleIndexes(VectorNPointMutation):
    """
    Uniform N Point indexes shuffle mutation.
    """

    def __init__(self, probability=1.0, arity=1, events=None, n=1):
        super().__init__(probability=probability, arity=arity, events=events, n=n)

    def attempt_operator(self, individuals, attempt_num):
        """
        Attempt to perform the mutation operator
        Parameters
        ----------
        individuals : list of individuals
            individuals to mutate
        attempt_num : int
            Current attempt number
        Returns
        ----------
        tuple of (bool, list of individuals)
            first return value determines if the the attempt succeeded
            second return value is the operator result
        """
        succeeded = True
        for individual in individuals:
            for i in range(self.n):
                if random.random() < self.probability:
                    swap_indx = random.randint(0, individual.size() - 2)
                    if swap_indx >= i:
                        swap_indx += 1
                    tmp = individual.cell_value(swap_indx)
                    individual.set_cell_value(swap_indx, individual.cell_value(i))
                    individual.set_cell_value(i, tmp)

        self.applied_individuals = individuals
        return succeeded, individuals
