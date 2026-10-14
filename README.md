# NumPy and Pandas Fundamentals

## Overview
This repository contains introductory Python examples for numerical arrays and tabular data manipulation, based on the supplied learning notes.

## Files
- `numpy_basics.py`: array creation, attributes, iteration, special arrays, vectorized calculations, CSV loading, and slicing.
- `pandas_basics.py`: Series, descriptive statistics, DataFrames, row/column selection, filtering, and cell updates.
- `requirements.txt`: Python library dependencies.
- `data/`: optional location for the `class-grades.csv` file referenced in the original notes.

## Requirements
Python 3.9+ is recommended. Install the required packages:

```bash
pip install -r requirements.txt
```

## Run
From the repository root:

```bash
python numpy_basics.py
python pandas_basics.py
```

The NumPy script runs its array examples without any data file. Its CSV-loading and slicing example is skipped unless `data/class-grades.csv` is present.

## Dataset note
The supplied PDF refers to a local `class-grades.csv` file, but that dataset was not included in the uploaded PDF. Do not upload course or personal data publicly unless you have permission to share it.
