from evokity.mutations import VectorShuffleIndexesMutation
from eckity.genetic_encodings.ga.bit_string_vector import BitStringVector
from eckity.fitness.simple_fitness import SimpleFitness


def test_shuffle_basic():
    "Test we get a permutation with shuffling probablity set to 1"
    mutator = VectorShuffleIndexesMutation(n=5)
    individual = BitStringVector(SimpleFitness(), length=5)
    individual.vector = [0, 1, 0, 1, 0]
    success, mutated_individuals = mutator.attempt_operator([individual.clone()], 1)
    assert success
    assert individual.get_vector() != mutated_individuals[0].get_vector()
    assert sorted(individual.get_vector()) == sorted(
        mutated_individuals[0].get_vector()
    )


def test_no_shuffle():
    "Test no mutation happens when mutation probablity is set to 0."
    mutator = VectorShuffleIndexesMutation(probability=0, n=5)
    individual = BitStringVector(SimpleFitness(), length=5)
    individual.vector = [0, 1, 0, 1, 0]
    success, mutated_individuals = mutator.attempt_operator([individual.clone()], 1)
    assert success
    assert individual.get_vector() == mutated_individuals[0].get_vector()
