from eckity.fitness.simple_fitness import SimpleFitness
from eckity.genetic_encodings.ga.float_vector import FloatVector

from evokity.crossovers import FloatVectorMeanCrossover


def test_float_vector_mean_crossover_basic():
    """Test we mean crossover with probability set to 1"""
    crossover = FloatVectorMeanCrossover()
    individual1 = FloatVector(SimpleFitness(), length=6)
    individual2 = FloatVector(SimpleFitness(), length=6)
    individual1.vector = [0.0] * 6
    individual2.vector = [1.0] * 6
    individuals = [individual1.clone(), individual2.clone()]
    mutated_individuals = crossover.apply(individuals)
    assert mutated_individuals[0].vector != individual1.vector
    assert mutated_individuals[1].vector != individual2.vector
    assert mutated_individuals[0].vector == [0.5] * 6
    assert mutated_individuals[1].vector == [0.5] * 6
