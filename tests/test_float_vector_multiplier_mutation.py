from eckity.fitness.simple_fitness import SimpleFitness
from eckity.genetic_encodings.ga.bit_string_vector import BitStringVector

from evokity.mutations import FloatVectorMultiplierNPointMutation


def test_multiplier_mutation_basic():
    """Test we get a permutation with multiplier probability set to 1"""
    mutator = FloatVectorMultiplierNPointMutation(n=8, left_bound=2, right_bound=4)
    individual1 = BitStringVector(SimpleFitness(), length=8)
    individual2 = BitStringVector(SimpleFitness(), length=8)
    individual1.vector = [0] * 8
    individual2.vector = [1] * 8
    individuals = [individual1.clone(), individual2.clone()]
    success, mutated_individuals = mutator.attempt_operator(individuals, 1)
    mutated_individual1 = mutated_individuals[0]
    mutated_individual2 = mutated_individuals[1]
    assert success
    assert mutated_individual1.vector == individual1.vector
    assert mutated_individual2.vector != individual2.vector
    assert all([2 <= val <= 4 for val in mutated_individual2.vector])
