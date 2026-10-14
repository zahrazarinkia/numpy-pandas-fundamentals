"""
NumPy Fundamentals
------------------
Examples adapted from the supplied NumpyAndPandas.pdf:
- Creating one-dimensional and multidimensional arrays
- Inspecting array attributes
- Iterating through arrays
- Creating arrays with special values
- Vectorized calculations
- Loading and slicing a numeric CSV file
"""

from pathlib import Path

import numpy as np


def array_creation_examples() -> None:
    """Create one-dimensional and two-dimensional arrays."""
    numbers = np.array([10, 20, 30, 40, 50])
    print("One-dimensional array:")
    print(type(numbers))
    print(numbers)

    integers = np.array([[10, 18, 4], [7, 14, 163], [11, 2, 53]])
    print("\nTwo-dimensional array:")
    print(integers)


def array_attributes_and_iteration() -> None:
    """Show common array attributes and iteration patterns."""
    integers = np.array([[10, 18, 4], [7, 14, 163], [11, 2, 53]])

    print("\nArray attributes:")
    print("dtype:", integers.dtype)
    print("ndim:", integers.ndim)
    print("shape:", integers.shape)
    print("size:", integers.size)
    print("itemsize:", integers.itemsize)

    print("\nIterate by row and column:")
    for row in integers:
        for column in row:
            print(column, end="   ")
        print()

    print("\nIterate over flattened array:")
    for value in integers.flat:
        print(value, end=", ")
    print()


def special_arrays() -> None:
    """Create arrays of zeros, ones, a constant value, and a range."""
    zero_array = np.zeros(8)
    ones_array = np.ones(6)
    full_array = np.full((3, 5), 2)
    range_array = np.arange(1, 10)

    print("\nZeros:", zero_array)
    print("Ones:", ones_array)
    print("Full array:\n", full_array)
    print("Range:", range_array)


def array_calculations() -> None:
    """Demonstrate vectorized arithmetic and in-place updates."""
    numbers = np.arange(1, 6)

    print("\nOriginal numbers:", numbers)
    print("Numbers multiplied by 2:", numbers * 2)
    print("Numbers cubed:", numbers**3)
    print("Original array remains unchanged after expressions:", numbers)

    numbers += 10
    print("After adding 10 in place:", numbers)


def load_and_slice_csv(csv_path: Path) -> None:
    """
    Load a numeric CSV file and demonstrate row-wise means and slicing.

    The source PDF refers to a local class-grades.csv file that was not
    included in the uploaded materials. Provide that file to run this example.
    """
    if not csv_path.exists():
        print(
            f"\nSkipping CSV example: {csv_path} was not found. "
            "Place class-grades.csv in the data/ folder to run this section."
        )
        return

    grades = np.loadtxt(csv_path, dtype=float, delimiter=",")
    print("\nRow-wise means:")
    print(grades.mean(axis=1))

    if grades.shape[0] > 16:
        print("Mean of row at index 16:", grades.mean(axis=1)[16])

    print("\nRows 1 to 2:")
    print(grades[1:3])
    print("\nColumn 2:")
    print(grades[:, 2:3])
    print("\nRows 1 to 2 and columns 2 to 4:")
    print(grades[1:3, 2:5])


def main() -> None:
    array_creation_examples()
    array_attributes_and_iteration()
    special_arrays()
    array_calculations()
    csv_path = Path("data") / "class-grades.csv"
    load_and_slice_csv(csv_path)


if __name__ == "__main__":
    main()
