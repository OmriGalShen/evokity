from eckity.fitness.simple_fitness import SimpleFitness
from eckity.genetic_encodings.ga.float_vector import FloatVector

from evokity.crossovers import FloatVectorBlendCrossover


def test_float_vector_blend_crossover_basic():
    """Test we blend crossover probability set to 1 and alpha = 0.5"""
    crossover = FloatVectorBlendCrossover()
    individual1 = FloatVector(SimpleFitness(), length=4)
    individual2 = FloatVector(SimpleFitness(), length=4)
    individual1.vector = [0.0, 0.0, 0.0, 0.0]
    individual2.vector = [1.0, 1.0, 1.0, 1.0]
    individuals = [individual1.clone(), individual2.clone()]
    mutated_individuals = crossover.apply(individuals)
    assert mutated_individuals[0].vector != individual1.vector
    assert mutated_individuals[1].vector != individual2.vector
    assert max(mutated_individuals[0].vector) > 0
    assert min(mutated_individuals[1].vector) < 1


def test_float_vector_blend_crossover_zero_alpha():
    """Test we blend crossover probability set to 1 and alpha = 0"""
    crossover = FloatVectorBlendCrossover(alpha=0)
    individual1 = FloatVector(SimpleFitness(), length=5)
    individual2 = FloatVector(SimpleFitness(), length=5)
    individual1.vector = [0.0, 0.0, 0.0, 0.0, 0.0]
    individual2.vector = [1.0, 1.0, 1.0, 1.0, 1.0]
    individuals = [individual1.clone(), individual2.clone()]
    mutated_individuals = crossover.apply(individuals)
    assert mutated_individuals[0].vector == individual1.vector
    assert mutated_individuals[1].vector == individual2.vector
