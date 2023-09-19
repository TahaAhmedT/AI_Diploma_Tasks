import pandas as pd
import numpy as np

df = pd.DataFrame({'height': [175, 180, np.nan, 170],
                   'weight': [70, np.nan, 80, 75]})
print(df)
print()

mean_height = df['height'].mean()
mean_weight = df['weight'].mean()

df = df.replace({'height': np.nan, 'weight': np.nan},
           {'height': mean_height, 'weight': mean_weight})

print(df)
