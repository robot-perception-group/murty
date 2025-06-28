# Murty Algorithm Python Bindings

This package provides Python bindings for the Murty algorithm, which is used for finding the k-best assignments in assignment problems.

## Installation

### From source

```bash
pip install .
```

### Development installation

```bash
pip install -e .
```

## Requirements

- Python 3.8+
- NumPy
- Eigen3 (C++ library)
- CMake 3.15+
- C++14 compatible compiler

## Usage

Here's how to use the `murty` function to get the k-best assignments.

```python
import numpy as np
from murty import murty

# Create a cost matrix
cost_matrix = np.array([
    [10, 20, 5],
    [15, 5, 10],
    [20, 15, 10]
], dtype=np.float64)

# Get the 3-best assignments
k = 3
assignments = murty(cost_matrix)

print(f"Top {k} assignments:")
for i, (cost, sol) in enumerate(assignments):
    if i >= k:
        break
    print(f"Assignment {i+1}:")
    print(f"  Cost: {cost}")
    print(f"  Solution: {sol}")
    # sol[i] = j means row i is assigned to column j
    for row, col in enumerate(sol):
        print(f"    Row {row} -> Col {col} (Cost: {cost_matrix[row, col]})")

```

This will output the top 3 assignments with their respective costs and solutions.

## Building

This package uses scikit-build-core for building. The C++ extension module `_murty` is built automatically when installing.

## Acknowledgements

This code is  an extraction of Jonatan Olofsson's
implementation of Murty's algorithm from his [MHT repo](https://github.com/jonatanolofsson/mht) with pybind.

## License

GPLv3