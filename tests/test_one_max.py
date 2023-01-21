import math

from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.creators.ga_creators.bit_string_vector_creator import (
    GABitStringVectorCreator,
)
from eckity.creators.ga_creators.float_vector_creator import GAFloatVectorCreator
from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
from eckity.genetic_operators.crossovers.vector_k_point_crossover import (
    VectorKPointsCrossover,
)
from eckity.genetic_operators.mutations.vector_random_mutation import (
    BitStringVectorNFlipMutation,
    FloatVectorUniformNPointMutation,
)
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from eckity.termination_checkers.threshold_from_target_termination_checker import (
    ThresholdFromTargetTerminationChecker,
)

from evokity.crossovers import (
    VectorUniformCrossover,
    FloatVectorBlendCrossover,
    FloatVectorMeanCrossover,
)
from evokity.mutations import (
    VectorShuffleIndexesNPointMutation,
    FloatVectorMultiplierNPointMutation,
)
from evokity.selection import (
    RouletteSelection,
    RandomSelection,
    StochasticUniversalSelection,
)


class OneMaxEvaluator(SimpleIndividualEvaluator):
    def _evaluate_individual(self, individual):
        """
        Compute the fitness value of a given individual.
        Parameters
        ----------
        individual: Vector
            The individual to compute the fitness value for.
        Returns
        -------
        float
            The evaluated fitness value of the given individual.
        """
        return sum(individual.vector)


def test_one_max_shuffle_indexes():
    """Test vector index shuffling mutation."""
    algo = SimpleEvolution(
        Subpopulation(
            creators=GABitStringVectorCreator(length=10),
            population_size=30,
            # user-defined fitness evaluation method
            evaluator=OneMaxEvaluator(),
            # maximization problem (fitness is sum of values), so higher fitness is better
            higher_is_better=True,
            elitism_rate=1 / 30,
            # genetic operators sequence to be applied in each generation
            operators_sequence=[
                VectorKPointsCrossover(probability=0.5, k=1),
                BitStringVectorNFlipMutation(
                    probability=0.2, probability_for_each=0.05, n=10
                ),
                VectorShuffleIndexesNPointMutation(probability=0.5, n=10),
            ],
            selection_methods=[
                # (selection method, selection probability) tuple
                (TournamentSelection(tournament_size=3, higher_is_better=True), 1)
            ],
        ),
        breeder=SimpleBreeder(),
        max_workers=4,
        max_generation=500,
        termination_checker=ThresholdFromTargetTerminationChecker(
            optimal=100, threshold=0.0
        ),
        statistics=BestAverageWorstStatistics(),
    )

    # evolve the generated initial population
    algo.evolve()

    best_solution = algo.execute()
    assert best_solution == [1] * 10


def test_one_max_multiplier_mutation():
    """Test float vector multiplier mutation."""
    # Initialize the evolutionary algorithm
    algo = SimpleEvolution(
        Subpopulation(
            creators=GAFloatVectorCreator(bounds=(0.0, 1.0), length=4),
            population_size=300,
            # user-defined fitness evaluation method
            evaluator=OneMaxEvaluator(),
            # maximization problem (fitness is sum of values), so higher fitness is better
            higher_is_better=True,
            elitism_rate=1 / 300,
            # genetic operators sequence to be applied in each generation
            operators_sequence=[
                VectorKPointsCrossover(probability=0.7, k=1),
                FloatVectorMultiplierNPointMutation(probability=0.3, n=2),
            ],
            selection_methods=[
                # (selection method, selection probability) tuple
                (TournamentSelection(tournament_size=3, higher_is_better=True), 1)
            ],
        ),
        breeder=SimpleBreeder(),
        max_workers=4,
        max_generation=500,
        termination_checker=ThresholdFromTargetTerminationChecker(
            optimal=100, threshold=0.0
        ),
        statistics=BestAverageWorstStatistics(),
    )

    # evolve the generated initial population
    algo.evolve()

    result = algo.execute()
    best_solution = [1.0] * 10
    tolerance = 0.05
    assert all(
        math.isclose(x, y, abs_tol=tolerance) for x, y in zip(result, best_solution)
    )


def test_one_max_uniform_crossover():
    "Test vector uniform crossover."
    algo = SimpleEvolution(
        Subpopulation(
            creators=GABitStringVectorCreator(length=10),
            population_size=30,
            # user-defined fitness evaluation method
            evaluator=OneMaxEvaluator(),
            # maximization problem (fitness is sum of values), so higher fitness is better
            higher_is_better=True,
            elitism_rate=1 / 30,
            # genetic operators sequence to be applied in each generation
            operators_sequence=[
                VectorUniformCrossover(probability=0.5),
                BitStringVectorNFlipMutation(
                    probability=0.2, probability_for_each=0.05, n=10
                ),
                VectorShuffleIndexesNPointMutation(probability=0.5, n=10),
            ],
            selection_methods=[
                # (selection method, selection probability) tuple
                (TournamentSelection(tournament_size=3, higher_is_better=True), 1)
            ],
        ),
        breeder=SimpleBreeder(),
        max_workers=4,
        max_generation=500,
        termination_checker=ThresholdFromTargetTerminationChecker(
            optimal=100, threshold=0.0
        ),
        statistics=BestAverageWorstStatistics(),
    )

    # evolve the generated initial population
    algo.evolve()

    best_solution = algo.execute()
    assert best_solution == [1] * 10


def test_one_max_float_vector_blend_crossover():
    # Initialize the evolutionary algorithm
    algo = SimpleEvolution(
        Subpopulation(
            creators=GAFloatVectorCreator(bounds=(0.0, 1.0), length=4),
            population_size=300,
            # user-defined fitness evaluation method
            evaluator=OneMaxEvaluator(),
            # maximization problem (fitness is sum of values), so higher fitness is better
            higher_is_better=True,
            elitism_rate=1 / 300,
            # genetic operators sequence to be applied in each generation
            operators_sequence=[
                FloatVectorBlendCrossover(probability=0.5),
                FloatVectorUniformNPointMutation(probability=0.3, n=2),
            ],
            selection_methods=[
                # (selection method, selection probability) tuple
                (TournamentSelection(tournament_size=3, higher_is_better=True), 1)
            ],
        ),
        breeder=SimpleBreeder(),
        max_workers=4,
        max_generation=500,
        termination_checker=ThresholdFromTargetTerminationChecker(
            optimal=100, threshold=0.0
        ),
        statistics=BestAverageWorstStatistics(),
    )

    # evolve the generated initial population
    algo.evolve()

    result = algo.execute()
    best_solution = [1.0] * 10
    tolerance = 0.05
    assert all(
        math.isclose(x, y, abs_tol=tolerance) for x, y in zip(result, best_solution)
    )


def test_one_max_float_vector_mean_crossover():
    # Initialize the evolutionary algorithm
    algo = SimpleEvolution(
        Subpopulation(
            creators=GAFloatVectorCreator(bounds=(0.0, 1.0), length=4),
            population_size=300,
            # user-defined fitness evaluation method
            evaluator=OneMaxEvaluator(),
            # maximization problem (fitness is sum of values), so higher fitness is better
            higher_is_better=True,
            elitism_rate=1 / 300,
            # genetic operators sequence to be applied in each generation
            operators_sequence=[
                FloatVectorMeanCrossover(probability=0.5),
                FloatVectorUniformNPointMutation(probability=0.3, n=2),
            ],
            selection_methods=[
                # (selection method, selection probability) tuple
                (TournamentSelection(tournament_size=3, higher_is_better=True), 1)
            ],
        ),
        breeder=SimpleBreeder(),
        max_workers=5,
        max_generation=500,
        termination_checker=ThresholdFromTargetTerminationChecker(
            optimal=100, threshold=0.0
        ),
        statistics=BestAverageWorstStatistics(),
    )

    # evolve the generated initial population
    algo.evolve()

    result = algo.execute()
    best_solution = [1.0] * 10
    tolerance = 0.05
    assert all(
        math.isclose(x, y, abs_tol=tolerance) for x, y in zip(result, best_solution)
    )


def test_one_max_roulette_selection():
    """Test roulette selection."""
    algo = SimpleEvolution(
        Subpopulation(
            creators=GABitStringVectorCreator(length=10),
            population_size=30,
            # user-defined fitness evaluation method
            evaluator=OneMaxEvaluator(),
            # maximization problem (fitness is sum of values), so higher fitness is better
            higher_is_better=True,
            elitism_rate=1 / 30,
            # genetic operators sequence to be applied in each generation
            operators_sequence=[
                VectorUniformCrossover(probability=0.5),
                BitStringVectorNFlipMutation(
                    probability=0.2, probability_for_each=0.05, n=10
                ),
                VectorShuffleIndexesNPointMutation(probability=0.5, n=10),
            ],
            selection_methods=[(RouletteSelection(k=3), 1)],
        ),
        breeder=SimpleBreeder(),
        max_workers=4,
        max_generation=2000,
        termination_checker=ThresholdFromTargetTerminationChecker(
            optimal=100, threshold=0.0
        ),
        statistics=BestAverageWorstStatistics(),
    )

    # evolve the generated initial population
    algo.evolve()

    best_solution = algo.execute()
    assert best_solution == [1] * 10


def test_one_max_random_selection():
    """Test roulette selection."""
    algo = SimpleEvolution(
        Subpopulation(
            creators=GABitStringVectorCreator(length=10),
            population_size=30,
            # user-defined fitness evaluation method
            evaluator=OneMaxEvaluator(),
            # maximization problem (fitness is sum of values), so higher fitness is better
            higher_is_better=True,
            elitism_rate=1 / 30,
            # genetic operators sequence to be applied in each generation
            operators_sequence=[
                VectorUniformCrossover(probability=0.5),
                BitStringVectorNFlipMutation(
                    probability=0.2, probability_for_each=0.05, n=10
                ),
                VectorShuffleIndexesNPointMutation(probability=0.5, n=10),
            ],
            selection_methods=[(RandomSelection(5), 1)],
        ),
        breeder=SimpleBreeder(),
        max_workers=4,
        max_generation=2000,
        termination_checker=ThresholdFromTargetTerminationChecker(
            optimal=100, threshold=0.0
        ),
        statistics=BestAverageWorstStatistics(),
    )

    # evolve the generated initial population
    algo.evolve()

    best_solution = algo.execute()
    assert best_solution == [1] * 10


def test_one_max_stochastic_selection():
    """Test stochastic selection."""
    algo = SimpleEvolution(
        Subpopulation(
            creators=GABitStringVectorCreator(length=10),
            population_size=30,
            # user-defined fitness evaluation method
            evaluator=OneMaxEvaluator(),
            # maximization problem (fitness is sum of values), so higher fitness is better
            higher_is_better=True,
            elitism_rate=1 / 30,
            # genetic operators sequence to be applied in each generation
            operators_sequence=[
                VectorUniformCrossover(probability=0.5),
                BitStringVectorNFlipMutation(
                    probability=0.2, probability_for_each=0.05, n=10
                ),
                VectorShuffleIndexesNPointMutation(probability=0.5, n=10),
            ],
            selection_methods=[(StochasticUniversalSelection(5), 1)],
        ),
        breeder=SimpleBreeder(),
        max_workers=4,
        max_generation=2000,
        termination_checker=ThresholdFromTargetTerminationChecker(
            optimal=100, threshold=0.0
        ),
        statistics=BestAverageWorstStatistics(),
    )

    # evolve the generated initial population
    algo.evolve()

    best_solution = algo.execute()
    assert best_solution == [1] * 10
