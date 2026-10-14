"""
Pandas Fundamentals
-------------------
Examples adapted from the supplied NumpyAndPandas.pdf:
- Creating Series with and without custom indices
- Descriptive statistics
- Creating and inspecting DataFrames
- Selecting rows and columns
- Boolean filtering
- Reading and updating a DataFrame cell
"""

import pandas as pd


def series_examples() -> None:
    """Create Series and inspect values and descriptive statistics."""
    grades = pd.Series([12, 17, 14])
    print("Series with default index:")
    print(grades)
    print("Value at index 1:", grades[1])
    print("\nDescriptive statistics:")
    print(grades.describe())

    named_grades = pd.Series(
        [11, 18, 19],
        index=["Ali", "Reza", "Mohammad"],
    )
    print("\nSeries with named index:")
    print(named_grades)
    print("Reza's value:", named_grades["Reza"])


def dataframe_examples() -> None:
    """Create a DataFrame and demonstrate common selection operations."""
    grades_dict = {
        "Mohammad": [11, 13, 17],
        "Reza": [16, 11, 19],
        "Zahra": [18, 12, 16],
    }
    grades = pd.DataFrame(grades_dict)
    print("\nDataFrame with default index:")
    print(grades)

    grades.index = ["Test1", "Test2", "Test3"]
    print("\nDataFrame with named rows:")
    print(grades)

    print("\nOne column:")
    print(grades["Mohammad"])
    print("\nColumn accessed as an attribute:")
    print(grades.Mohammad)

    print("\nRow selected with loc:")
    print(grades.loc["Test1"])
    print("\nFirst row selected with iloc:")
    print(grades.iloc[0])

    print("\nValues greater than 14 (other cells become NaN):")
    print(grades[grades > 14])

    print("\nSingle cell using at:")
    print(grades.at["Test1", "Reza"])

    grades.at["Test1", "Reza"] = 20
    print("\nAfter updating Test1/Reza to 20:")
    print(grades)


def main() -> None:
    series_examples()
    dataframe_examples()


if __name__ == "__main__":
    main()
