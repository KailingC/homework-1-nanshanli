"""Spring 2019 COMSW 4995: Applied Machine Learning.

UNI: nl2643
Homework 1 Task 1.3

Use pandas to read 'input.txt' and test the number of rows, columns and
sum of the '2010' column.

"""

import pandas as pd

df = pd.read_csv('task1/input.txt', sep=',', escapechar='\\', index_col=0)
df['2010'] = pd.to_numeric(df['2010'], errors='coerce')


def test_row():
    """Check row number in df."""
    assert len(df) == 225


def test_column():
    """Check column number in df."""
    assert len(df.columns) == 31


def test_population():
    """Check sum of '2010' column in df."""
    assert round(df['2010'].sum()) == 7065
