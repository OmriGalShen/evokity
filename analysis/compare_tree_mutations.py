from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.creators.gp_creators.ramped_hh import RampedHalfAndHalfCreator
from eckity.genetic_encodings.gp.tree.functions import f_add, f_mul, f_sub, f_div, f_sqrt, f_log, f_abs, f_max, f_min, \
    f_inv, f_neg
from eckity.genetic_operators.crossovers.subtree_crossover import SubtreeCrossover
from eckity.genetic_operators.mutations.erc_mutation import ERCMutation
from eckity.genetic_operators.mutations.subtree_mutation import SubtreeMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from eckity.termination_checkers.threshold_from_target_termination_checker import ThresholdFromTargetTerminationChecker
from examples.treegp.non_sklearn_mode.symbolic_regression.sym_reg_evaluator import SymbolicRegressionEvaluator

from analysis.analysis_utils import display_results, TestOperatorWrapper
from evokity.mutations import TreeShrinkMutation


def compare_tree_mutations():
    repeats = 20
    threshold = 1e-5
    probability = 0.5
    test_subjects = [
        TestOperatorWrapper("Subtree",
                            SubtreeMutation(probability=probability)),
        TestOperatorWrapper("TreeShrink", TreeShrinkMutation(probability=probability, max_iterations=20)),
    ]
    for test_subject in test_subjects:
        mutation = test_subject.test_operator
        result = tree_one_max_mutation_runner(repeats=repeats, threshold=threshold,
                                              mutation=mutation)
        test_subject.result = result

    display_results(test_operators=test_subjects,
                    repeats=repeats,
                    x_label='Mutations (best to worst)',
                    title='Tree Mutations Comparison')


def tree_one_max_mutation_runner(repeats, threshold, mutation):
    total_generations = 0
    function_set = [
        f_add,
        f_mul,
        f_sub,
        f_div,
        f_sqrt,
        f_log,
        f_abs,
        f_max,
        f_min,
        f_inv,
        f_neg,
    ]
    for iteration in range(repeats):
        terminal_set = ["x", "y", "z", 0, 1, -1]

        algo = SimpleEvolution(
            Subpopulation(
                creators=RampedHalfAndHalfCreator(
                    init_depth=(2, 4),
                    terminal_set=terminal_set,
                    function_set=function_set,
                    bloat_weight=0.0001,
                ),
                population_size=400,
                # user-defined fitness evaluation method
                evaluator=SymbolicRegressionEvaluator(),
                # minimization problem (fitness is MAE), so higher fitness is worse
                higher_is_better=False,
                elitism_rate=0.05,
                # genetic operators sequence to be applied in each generation
                operators_sequence=[
                    SubtreeCrossover(probability=0.4, arity=2),
                    # SubtreeMutation(probability=0.2, arity=1),
                    # TreeShrinkMutation(probability=0),
                    mutation,
                    ERCMutation(probability=0.05, arity=1),
                ],
                selection_methods=[
                    # (selection method, selection probability) tuple
                    (TournamentSelection(tournament_size=3, higher_is_better=False), 1)
                ],
            ),
            breeder=SimpleBreeder(),
            max_workers=4,
            max_generation=10000,
            # random_seed=0,
            termination_checker=ThresholdFromTargetTerminationChecker(
                optimal=0, threshold=threshold
            ),
            statistics=BestAverageWorstStatistics(),
        )

        algo.evolve()
        algo.execute(x=2, y=3, z=4)
        total_generations += algo.final_generation_
        print(f'\nIteration:{iteration}\n')
    return total_generations / repeats


if __name__ == '__main__':
    compare_tree_mutations()
