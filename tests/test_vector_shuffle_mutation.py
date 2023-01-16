from eckity.fitness.simple_fitness import SimpleFitness
from eckity.genetic_encodings.ga.bit_string_vector import BitStringVector

from evokity.mutations import VectorShuffleIndexesMutation


def test_shuffle_basic():
    """Test we get a permutation with shuffling probability set to 1"""
    mutator = VectorShuffleIndexesMutation(n=5)
    individual = BitStringVector(SimpleFitness(), length=5)
    individual.vector = [0, 1, 0, 1, 0]
    individuals = [individual.clone()]
    success, mutated_individuals = mutator.attempt_operator(individuals, 1)
    mutated_individual = mutated_individuals[0]
    assert success
    assert individual.get_vector() != mutated_individual.get_vector()
    assert sorted(individual.get_vector()) == sorted(mutated_individual.get_vector())


def test_no_shuffle():
    """Test no mutation happens when mutation probability is set to 0."""
    mutator = VectorShuffleIndexesMutation(probability=0, n=5)
    individual = BitStringVector(SimpleFitness(), length=5)
    individual.vector = [0, 1, 0, 1, 0]
    individuals = [individual.clone()]
    success, mutated_individuals = mutator.attempt_operator(individuals, 1)
    mutated_individual = mutated_individuals[0]
    assert success
    assert individual.get_vector() == mutated_individual.get_vector()
