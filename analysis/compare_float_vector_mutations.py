from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.creators.ga_creators.float_vector_creator import GAFloatVectorCreator
from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
from eckity.genetic_operators.crossovers.vector_k_point_crossover import VectorKPointsCrossover
from eckity.genetic_operators.mutations.vector_random_mutation import FloatVectorUniformNPointMutation, \
    FloatVectorGaussNPointMutation, FloatVectorGaussOnePointMutation, FloatVectorUniformOnePointMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from eckity.termination_checkers.threshold_from_target_termination_checker import ThresholdFromTargetTerminationChecker

from analysis.analysis_utils import TestOperatorWrapper, display_results
from evokity.mutations import FloatVectorMultiplierNPointMutation, VectorShuffleIndexesNPointMutation


class OneMaxEvaluator(SimpleIndividualEvaluator):
    def _evaluate_individual(self, individual):
        return sum(individual.vector)


def compare_float_vector_mutations():
    repeats = 100
    threshold = 0.1
    length = 10
    probability = 0.3
    test_operators = [
        TestOperatorWrapper("Multiplier 0-1",
                            FloatVectorMultiplierNPointMutation(probability=probability, n=length, left_bound=0.,
                                                                right_bound=1.)),
        TestOperatorWrapper("Shuffle", VectorShuffleIndexesNPointMutation(probability=probability, n=length)),
        TestOperatorWrapper("Uniform N",
                            FloatVectorUniformNPointMutation(probability=probability, n=length)),
        TestOperatorWrapper("Gauss N", FloatVectorGaussNPointMutation(probability=probability, n=length)),
        TestOperatorWrapper("Gauss 1",
                            FloatVectorGaussOnePointMutation(probability=probability)),
        TestOperatorWrapper("Uniform 1",
                            FloatVectorUniformOnePointMutation(probability=probability)),
    ]
    for test_class in test_operators:
        mutation = test_class.test_operator
        result = float_vector_one_max_mutation_runner(repeats=repeats, threshold=threshold,
                                                      mutation=mutation, length=length)
        test_class.result = result

    display_results(test_operators=test_operators,
                    repeats=repeats,
                    x_label='Mutations (best to worst)',
                    title='FloatVector Mutations Comparison')


def float_vector_one_max_mutation_runner(repeats, threshold, mutation, length):
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
                    VectorKPointsCrossover(probability=0.7, k=1),
                    FloatVectorUniformNPointMutation(probability=0.1, n=1),
                    mutation,
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
    compare_float_vector_mutations()
