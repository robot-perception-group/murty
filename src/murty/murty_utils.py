# standard library imports
from typing import Generator, Tuple

# third party imports
import numpy as np
from numpy.typing import NDArray

# local Application imports
from . import Murty

def murty(C: NDArray[np.float64]) -> Generator[Tuple[float, NDArray[np.int_]], None, None]:
    """Algorithm due to Murty for k-best assignments problem.
    
    This function generates assignments in non-decreasing order of cost.
    It uses Murty's algorithm to find k-best solutions to the linear assignment problem.
    
    Args:
        C: Cost matrix where C[i,j] is the cost of assigning row i to column j
        
    Yields:
        Tuple containing:
            - cost: The cost of the current assignment
            - sol: The assignment solution as an array where sol[i] = j means row i is assigned to column j
            
    Note:
        The algorithm will continue yielding solutions until exhausted.
        If no valid assignment exists, the function returns None.
    """
    mgen = Murty(C)
    while True:
        ok, cost, sol = mgen.draw()
        if not ok:
            return None
        yield cost, sol