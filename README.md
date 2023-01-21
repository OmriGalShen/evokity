<center><h1>Evokity</h1></center>

<p align="center">
Collection of essential <a href=https://github.com/EC-KitY/EC-KitY> Evolutionary Computation Kit</a> utilities
</p>

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/amitkummer/evolutionary-mini-project/integration.yaml?label=Tests%2C%20Linting%20%26%20Formatting&style=for-the-badge">
</p>

# Table of Contents

1. [Introduction](#introduction)
2. [Development](#development)
3. [Project Structure and Interface](#project-structure-and-interface)
4. [Analysis](#analysis)
5. [Final Thoughts](#final-thoughts)
6. [About](#about)

## Introduction

<a href=https://github.com/EC-KitY/EC-KitY> EC-KitY </a>
is comprehensive toolkit evolutionary computation algorithms written in Python.  <br/>
<strong>Evokity</strong> is an evolutionary computation collection that serves as extension and complement library to EC-KitY.  

#### Motivation

EC-KitY is an accessible and generic tool kit for doing evolutionary computation,  
we saw potential to add variety of utility classes to extend it.

#### Evokity Main Goals:

- Extend EC-KitY with new capabilities using new operators such as crossover, mutations and selections.
- New operators can be served to accommodate both Genetic Algorithm (GA) and tree-based Genetic Programming (GP) which
  are used in
  EC-KitY.
- Easy to maintain and extend project with emphasise on unit tests, linting & formatting and continuous integration.
- Project is public, free and accessible.

#### Currently Supported Operators:

| Crossover operators      | Mutations operators                 | Selection operators          |
|--------------------------|-------------------------------------|------------------------------|
| VectorUniformCrossover   | VectorShuffleIndexesMutation        | RouletteSelection            |
| VectorBlendCrossover     | TreeShrinkMutation                  | RandomSelection              |
| FloatVectorMeanCrossover | FloatVectorMultiplierNPointMutation | StochasticUniversalSelection |

#### Future Ideas and Goals:

Add more utility classes to be used with EC-KitY such:

- New Statistics
- New Genetic encoding
- New Breeder
- Etc.

## Development

Requires `poetry` installed (tested with `v1.2.2`) [See Docs](https://python-poetry.org/docs/).

Install the dependencies:

```sh
poetry install
```

Spawn a shell within the project's environment:

```
poetry shell
```

### Unit Tests

To run the unit-tests, use:

```
pytest
pytest -s // To show captured stdout.
```

### Formatting

To run formatting, use:

```
black evokity tests
```

## Project Structure and Interface

Currently, Evokity supports 7 genetic operators:  
2 crossovers, 2 mutations and 3 selections.

Category: Crossovers  
File: '.evokity/crossovers.py'

| Name            | VectorUniformCrossover | VectorBlendCrossover | FloatVectorMeanCrossover |
|-----------------|------------------------|----------------------|--------------------------|
| Name            |                        |                      |                          |
| Description     |                        |                      |                          | 
| Individual Type |                        |                      |                          |
| Parameters      |                        |                      |                          |
| Tests           |                        |                      |                          |

Category: Mutation  
File: 'evokity/mutations.py'

| Name            | VectorShuffleIndexesMutation | TreeShrinkMutation | FloatVectorMultiplierNPointMutation |
|-----------------|------------------------------|--------------------|-------------------------------------|
| Name            |                              |                    |                                     |
| Description     |                              |                    |                                     | 
| Individual Type |                              |                    |                                     |
| Parameters      |                              |                    |                                     |
| Tests           |                              |                    |                                     |

Category: Selections  
File: 'evokity/selection.py'

| Name            | RouletteSelection | RandomSelection | StochasticUniversalSelection |
|-----------------|-------------------|-----------------|------------------------------|
| Name            |                   |                 |                              |
| Description     |                   |                 |                              | 
| Individual Type |                   |                 |                              |
| Parameters      |                   |                 |                              |
| Tests           |                   |                 |                              |

## Analysis

![Alt text](/analysis/results_images/float_vector_mutations.png?raw=true "Optional Title")

## Final Thoughts

TODO

## About

### Authors

[Amit Kummer](https://github.com/amitkummer "Amit Kummer"),  
[Omri Gal Shenhav](https://github.com/OmriGalShen "Omri Gal Shenhav")

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
