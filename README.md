# Key Algorithms

This Python project is a simple implementation of three different exponential functions. Users can select which function to run by specifying a choice variable and providing the necessary parameters (A, E, M).

## Exponential Functions

The project contains three exponential functions:

1. **Naive Exponential** - Computes (A^E) % M, where A is the base, E is the exponent, and M is the modulus.

2. **Less Intelligent Exponential** - Computes the product of A^(k×2^count) with % M at the end.

3. **Intelligent Exponential** - Computes the product of (A^(k×2^count))% M with % M at the end.

## Usage

To run the program, execute the Python file `keyAlgorithms.py`. The program will prompt you to select one of the three exponential functions and provide the required parameter values.

```bash
python3 keyAlgorithms.py

## Authors

This project has been developed by Giorgio Tentorio and Gabriele Meles.
