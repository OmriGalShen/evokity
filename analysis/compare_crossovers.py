from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.creators.ga_creators.float_vector_creator import GAFloatVectorCreator
from eckity.genetic_operators.crossovers.vector_k_point_crossover import VectorKPointsCrossover
from eckity.genetic_operators.mutations.vector_random_mutation import FloatVectorUniformNPointMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from eckity.termination_checkers.threshold_from_target_termination_checker import ThresholdFromTargetTerminationChecker

from analysis.analysis_utils import TestOperatorWrapper, display_results, OneMaxEvaluator
from evokity.crossovers import VectorUniformCrossover, FloatVectorBlendCrossover, FloatVectorMeanCrossover


def compare_crossovers():
    repeats = 100
    length = 10
    threshold = 0.1
    probability = 0.3
    test_operators = [
        TestOperatorWrapper("K-1",
                            VectorKPointsCrossover(probability=probability, k=1)),
        TestOperatorWrapper("K-5",
                            VectorKPointsCrossover(probability=probability, k=5)),
        TestOperatorWrapper("K-10",
                            VectorKPointsCrossover(probability=probability, k=10)),
        TestOperatorWrapper("Uniform",
                            VectorUniformCrossover(probability=probability)),
        TestOperatorWrapper("Blend",
                            FloatVectorBlendCrossover(probability=probability)),
        TestOperatorWrapper("Mean",
                            FloatVectorMeanCrossover(probability=probability)),
    ]
    for test_class in test_operators:
        crossover = test_class.test_operator
        result = float_vector_one_max_crossover_runner(repeats=repeats, threshold=threshold, crossover=crossover,
                                                       length=length)
        test_class.result = result

    display_results(test_operators=test_operators,
                    repeats=repeats,
                    x_label='Crossovers (best to worst)',
                    title='Crossovers Comparison')


def float_vector_one_max_crossover_runner(repeats, threshold, crossover, length):
    total_generations = 0
    for _ in range(repeats):
        algo = SimpleEvolution(
            Subpopulation(
                creators=GAFloatVectorCreator(bounds=(0.0, 1.0), length=length),
                population_size=300,
                evaluator=OneMaxEvaluator(),
                higher_is_better=True,
                elitism_rate=1 / 300,
                operators_sequence=[
                    crossover,
                    FloatVectorUniformNPointMutation(probability=0.1, n=1),
                ],
                selection_methods=[
                    (TournamentSelection(tournament_size=3, higher_is_better=True), 1)
                ],
            ),
            breeder=SimpleBreeder(),
            max_workers=4,
            max_generation=1000,
            termination_checker=ThresholdFromTargetTerminationChecker(
                optimal=length, threshold=threshold
            ),
            statistics=BestAverageWorstStatistics(),
        )
        algo.evolve()
        algo.execute()
        total_generations += algo.final_generation_
    return total_generations / repeats


if __name__ == '__main__':
    compare_crossovers()
