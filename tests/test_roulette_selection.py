from evokity.selection import RouletteSelection
from eckity.genetic_encodings.ga.bit_string_vector import BitStringVector
from eckity.fitness.simple_fitness import SimpleFitness


def test_vector_roulette_selction():
    "Test roulette selection on vector individuals."
    selection = RouletteSelection(1)
    individual1 = BitStringVector(SimpleFitness(fitness=0.1), length=5)
    individual2 = BitStringVector(SimpleFitness(fitness=0.2), length=5)
    individual1.vector = [0, 0, 0, 0, 0]
    individual2.vector = [1, 1, 1, 1, 1]

    
    individuals = [individual1, individual2]
    selected = selection.select(individuals, [])
    assert len(selected) == 1
    individuals = [ind.vector for ind in individuals]
    assert selected[0].vector in individuals
