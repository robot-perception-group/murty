"""
Murty's algorithm for k-best linear assignment problems.
"""

try:
    # Try relative import first
    from ._murty import Murty
    from .murty_utils import murty
except ImportError as e:
    raise ImportError(f"Failed to import the compiled '_murty' extension module: {e}")

# Define the symbols to export when importing from this module
__all__ = ["Murty", "murty"]
