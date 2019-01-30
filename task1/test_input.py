import pandas as pd

df = pd.read_csv('task1/input.txt', sep = ',')
df['2010'] = pd.to_numeric(df['2010'], errors = 'coerce')

def test_row():
    assert len(df) == 225

def test_column():
    assert len(df.columns) == 32

def test_population():
    assert round(df['2010'].sum()) == 7065
