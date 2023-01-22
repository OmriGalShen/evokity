from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.creators.ga_creators.float_vector_creator import GAFloatVectorCreator
from eckity.genetic_operators.mutations.vector_random_mutation import (
    FloatVectorUniformNPointMutation,
)
from eckity.genetic_operators.selections.elitism_selection import ElitismSelection
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from eckity.termination_checkers.threshold_from_target_termination_checker import (
    ThresholdFromTargetTerminationChecker,
)

from analysis.analysis_utils import (
    TestOperatorWrapper,
    display_results,
    OneMaxEvaluator,
)
from evokity.mutations import VectorShuffleIndexesNPointMutation
from evokity.selection import RouletteSelection, StochasticUniversalSelection


def compare_selection():
    repeats = 100
    threshold = 0.18
    length = 5
    test_operators = [
        TestOperatorWrapper(
            "Tournament 3",
            TournamentSelection(tournament_size=3, higher_is_better=True),
        ),
        TestOperatorWrapper(
            "Tournament 5",
            TournamentSelection(tournament_size=5, higher_is_better=True),
        ),
        TestOperatorWrapper(
            "Elitism 1", ElitismSelection(num_elites=1, higher_is_better=True)
        ),
        TestOperatorWrapper(
            "Elitism 3", ElitismSelection(num_elites=3, higher_is_better=True)
        ),
        TestOperatorWrapper(
            "Elitism 10", ElitismSelection(num_elites=10, higher_is_better=True)
        ),
        TestOperatorWrapper(
            "Roulette  k-3", RouletteSelection(higher_is_better=True, k=3)
        ),
        TestOperatorWrapper(
            "Roulette  k-5", RouletteSelection(higher_is_better=True, k=5)
        ),
        TestOperatorWrapper(
            "Roulette  k-10", RouletteSelection(higher_is_better=True, k=5)
        ),
        TestOperatorWrapper(
            "Stochastic k=3", StochasticUniversalSelection(higher_is_better=True, k=3)
        ),
        TestOperatorWrapper(
            "Stochastic k=5", StochasticUniversalSelection(higher_is_better=True, k=5)
        ),
        # TestOperatorWrapper("Random k-1",
        #                     RandomSelection(higher_is_better=True, k=1)),
        # TestOperatorWrapper("Random k-3",
        #                     RandomSelection(higher_is_better=True, k=3)),
    ]
    for test_class in test_operators:
        selection = test_class.test_operator
        result = float_vector_one_max_selection_runner(
            repeats=repeats, threshold=threshold, selection=selection, length=length
        )
        test_class.result = result

    display_results(
        test_operators=test_operators,
        repeats=repeats,
        x_label="Selections (best to worst)",
        title="Selection Comparison",
    )


def float_vector_one_max_selection_runner(repeats, threshold, selection, length):
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
                    VectorShuffleIndexesNPointMutation(probability=0.2, n=length),
                    FloatVectorUniformNPointMutation(probability=0.2, n=1),
                    # FloatVectorUniformNPointMutation(probability=0.5, n=1),
                ],
                selection_methods=[(selection, 1)],
            ),
            breeder=SimpleBreeder(),
            max_workers=4,
            max_generation=100000,
            termination_checker=ThresholdFromTargetTerminationChecker(
                optimal=length, threshold=threshold
            ),
            statistics=BestAverageWorstStatistics(),
        )
        algo.evolve()
        algo.execute()
        total_generations += algo.final_generation_
    return total_generations / repeats


if __name__ == "__main__":
    compare_selection()
