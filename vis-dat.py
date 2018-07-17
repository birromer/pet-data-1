import numpy as np
import pandas as pd

df = pd.read_csv('AvalDiscente_20xx-x.csv', sep=';', error_bad_lines=False)

header = list(df.columns.values) #list with column names

for h in header[2:-1]:
    #replaces NaN values with None
    df[h][df[h].isnull()] = None

if __name__ == "__main__":
    print(df)
