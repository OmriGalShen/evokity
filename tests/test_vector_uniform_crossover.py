from eckity.fitness.simple_fitness import SimpleFitness
from eckity.genetic_encodings.ga.bit_string_vector import BitStringVector

from evokity.crossovers import VectorUniformCrossover


def test_uniform_crossover_basic():
    """Test we get a permutation with shuffling probability set to 1"""
    crossover = VectorUniformCrossover()
    individual1 = BitStringVector(SimpleFitness(), length=5)
    individual2 = BitStringVector(SimpleFitness(), length=5)
    individual1.vector = [0, 0, 0, 0, 0]
    individual2.vector = [1, 1, 1, 1, 1]
    individuals = [individual1.clone(), individual2.clone()]
    mutated_individuals = crossover.apply(individuals)
    assert mutated_individuals[0].vector != individual1.vector
    assert mutated_individuals[1].vector != individual2.vector
    assert mutated_individuals[1].vector == individual1.vector
    assert mutated_individuals[0].vector == individual2.vector
