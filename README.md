<center><h1>Evokity</h1></center>

<p align="center">
Collection of essential <a href=https://github.com/EC-KitY/EC-KitY> Evolutionary Computation Kit</a> utilities.
</p>

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/amitkummer/evolutionary-mini-project/integration.yaml?label=Tests%2C%20Linting%20%26%20Formatting&style=for-the-badge">
</p>

- [About](#about)
- [API](#api)
- [Analysis](#analysis)
- [Final Thoughts](#final-thoughts)
- [Development](#development)

# About

Evokity is a collection of crossover, mutation and selection operators for [EC-KitY](https://github.com/EC-KitY/EC-KitY).

## Evokity Operators

| Crossover                | Mutation                            | Selection                    |
| ------------------------ | ----------------------------------- | ---------------------------- |
| VectorUniformCrossover   | VectorShuffleIndexesMutation        | RouletteSelection            |
| VectorBlendCrossover     | TreeShrinkMutation                  | RandomSelection              |
| FloatVectorMeanCrossover | FloatVectorMultiplierNPointMutation | StochasticUniversalSelection |

## Why Create Evokity

While being an accessible and generic tool for performing evolutionary computations, EC-KitY
leaves room for desire when it comes to operators.

At the time of writing, EC-KitY offers only a single operator for doing vectors crossover.

## Design Goals

- Enhance EC-KitY with a variety of operators to complement existing ones.
- Operators for both Genetic Programming (GP) and Genetic Algorithms (GA).
- Extensive unit-testing, linting and formatting on push and pull requests.
- Accessible for cotributions.
- Dependency free.

## Future Ideas and Goals:

- Improved execution statistics.
- Genetic encoding.
- Wider range of Breeders.
- Support more frameworks.

# API

Evokity has 9 genetic operators -- 3 for crossover, 3 for mutation and 3 for selection.

## Crossover

evokity.crossovers.**VectorUniformCrossover**(probability=1, events=None)

Vector uniform crossover. Given 2 vectors, for every corresponding elements (same indices) preform
a swap in values.

- probability: `float`

  The probability of the crossover operator to be applied to each vector element.

- events: `list[string]`

  Events to publish before/after the mutation operator.

evokity.crossovers.**FloatVectorBlendCrossover**(probability=1, alpha=0.5, events=None)

Float Vector Blend crossover. Given 2 vectors, for every corresponding elements (same indices)
preform a blend in values.

- probability : `float`

  The probability of the crossover operator to be applied to each vector element.

- alpha: `float`

  The extent of the interval in which the new values can be drawn,
  for each element on both side of the parents.

- events: `list[string]`

  Events to publish before/after the mutation operator

evokity.crossover.**FloatVectorMeanCrossover**(probability=1, events=None)

Vector mean crossover. Given 2 vectors, for every corresponding elements (same indices),
replace them with the mean of the elemtnts.

- probability: `float`

  The probability of the crossover operator to be applied to each vector element.

- events: `list[string]`

  Events to publish before/after the mutation operator.

## Mutation

evokity.mutations.**VectorShuffleIndexesNPointMutation**(probability=1.0, events=None, n=2)

Uniform N Point indexes shuffle mutation.

- n: `int`

  Number of individuals to mutate at a time.

- probability: `float`

  The probability of the mutation operator to be applied to each vector element.

- events: `list[string]`

  Events to publish before/after the mutation operator.

evokity.mutations.**TreeShrinkMutation**(probability=1, max_iterations=100, events=None)

Shrink the individual by choosing randomly a branch and replacing it with one of the branch's arguments (also randomly chosen).

- max_iterations: `int`

  Maximum number of times mutation is tried to be applied.

- probability: `float`

  The probability of the mutation operator to be applied to each vector element.

- events: `list[string]`

  Events to publish before/after the mutation operator.

evokity.mutations.**FloatVectorMultiplierNPointMutation**(probability=1.0, left_bound=0.0, right_bound=1.0, events=None)

N Point Float Vector Multiplier Mutation. Randomly choose N vector cells and multiply them with a random variable between given bounds.

- probability: `float`

  The probability of the mutation operator to be applied to each vector element.

- left_bound: `float`

  The left bound (inclusive) for the random multiplier used to change the value of chosen vector cell.

- right_bound: `float`

  The right bound (inclusive) for the random multiplier used to change the value of chosen vector cell.

- events: `list[string]`

  Events to publish before/after the mutation operator.

## Selection

evokity.selection**RouletteSelection**(k: int, higher_is_better=False, events=None)

Select k individuals based on their fitness and a random roulette spin.

- k: `int`

  Number of selected individuals.

- higher_is_better: `bool`

  Higher fitness is better. If set to False, lower fitness is better.

- events: `list[string]`

  Events to publish before/after the mutation operator.

evokity.selection.**RandomSelection**(k: int, higher_is_better=False, events=None)

Randomly select k individuals.

- k: `int`

  Number of selected individuals.

- higher_is_better: `bool`

  Higher fitness is better. If set to False, lower fitness is better.

- events: `list[string]`

  Events to publish before/after the mutation operator.

evokity.selection.**StochasticUniversalSelection**(k: int, higher_is_better=False, events=None)

Select k individuals using stochastic universal sampling.

- k: `int`

  Number of selected individuals.

- higher_is_better: `bool`

  Higher fitness is better. If set to False, lower fitness is better.

- events: `list[string]`

  Events to publish before/after the mutation operator.

# Analysis

This section contains plots comparing how fast examples from EC-KitY
(symbolic regression and one-max)
converge to a solution, when using the different operators.

Each plot includes the average generation for the example to converge to
a solution using one of Evokity's operators.

The scripts for creating these plots can be found in the `analysis` directory.

## Mutations

![Alt text](/analysis/results_images/float_vector_mutations.png?raw=true)
![Alt text](/analysis/results_images/tree_mutations.png?raw=true)

## Selections

![Alt text](/analysis/results_images/selections.png?raw=true)

Note that RandomSelection is not included in the plot, as it does not coverage to a solution.
It is an interesting selection operator, but not the most useful one when it comes to practical uses.

## Crossovers

![Alt text](/analysis/results_images/crossovers.png?raw=true)

# Final Thoughts

Working with EC-KitY was a fairly straightforward and smooth exprience, thanks to the fact that it's open-source
and has various examples, which cover most use cases.

To help with rapid development, we created a simple CI using GitHub Actions for running unit-tests, linting and formatting on each push and pull request. This helped the development process a lot, by assuring unit tests are not randomly failing, code quality is not decreasing and readability is at a satisfactory level.

# Created By

- [Amit Kummer](https://github.com/amitkummer "Amit Kummer").
- [Omri Gal Shenhav](https://github.com/OmriGalShen "Omri Gal Shenhav").

### Citation

```
@article{eckity2022,
    author = {Sipper, Moshe and Halperin, Tomer and Tzruia, Itai and  Elyasaf, Achiya},
    title = {{EC-KitY}: Evolutionary Computation Tool Kit in {Python}},
    publisher = {arXiv},
    year = {2022},
    url = {https://arxiv.org/abs/2207.10367},
    doi = {10.48550/ARXIV.2207.10367},
}

@misc{eckity2022git,
    author = {Sipper, Moshe and Halperin, Tomer and Tzruia, Itai and  Elyasaf, Achiya},
    title = {{EC-KitY}: Evolutionary Computation Tool Kit in {Python}},
    year = {2022},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://www.eckity.org/} }
}

```

# Development

Requires `poetry` installed (tested with `v1.2.2`) [See Docs](https://python-poetry.org/docs/).

Install the dependencies:

```sh
poetry install --all-extras
```

Spawn a shell within the project's environment:

```sh
poetry shell
```

## Unit Tests

To run the unit-tests, use:

```sh
pytest
```

## Formatting

To run formatting, use:

```sh
black evokity tests
```
