from evokity.crossovers import VectorUniformCrossover
from eckity.genetic_encodings.ga.bit_string_vector import BitStringVector
from eckity.fitness.simple_fitness import SimpleFitness


def test_uniform_crossover_basic():
    "Test we get a permutation with shuffling probablity set to 1"
    crossover = VectorUniformCrossover()
    individual1 = BitStringVector(SimpleFitness(), length=5)
    individual2 = BitStringVector(SimpleFitness(), length=5)
    individual1.vector = [0, 0, 0, 0, 0]
    individual2.vector = [1, 1, 1, 1, 1]
    mutated_individuals = crossover.apply([individual1, individual2])
    assert individual1.vector != mutated_individuals[0]
    assert individual2.vector != mutated_individuals[1]
    assert individual1.vector == mutated_individuals[1].vector
    assert individual2.vector == mutated_individuals[0].vector
