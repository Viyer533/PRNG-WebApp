# A novel pseudo-random number generator based on multivariable optimization for image-cryptographic applications
Project to implement a Pseudo Random Number Generator (PRNG) using Elliptic Curve (EC) and Genetic Algorithm (GA) for image cryptographic applications. \
Based on the paper: [A novel pseudo-random number generator based on multivariable
optimization for image-cryptographic applications](https://www.sciencedirect.com/science/article/pii/S0957417423029482?via%3Dihub) by Takreem Haider, Saúl A. Blanco, Umar Hayat 

## Pseudo Random Number Generator (PRNG)
A pseudorandom number generator (PRNG) is a computational algorithm designed to generate sequences of numbers that appear random. However, these sequences are entirely determined by an initial value known as the seed value or key. \
With knowledge of the seed value and the algorithm used, one can reproduce the seemingly random results generated by the PRNG. Therefore, PRNGs produce sequences of numbers that are deterministic based on the initial seed value and algorithm, despite appearing random.

## Setup

1. Use `poetry` to install dependencies:

```bash
poetry install
```
2. Run `src/main.py` to generate the PRNS

```bash
poetry run python main.py
```
