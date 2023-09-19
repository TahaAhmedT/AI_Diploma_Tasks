import pandas as pd
import numpy as np
data = [(3, 5, 7), (2, 4, 6), (5, 8, 9)]
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print("Original DataFrame: ")
print(df)

df2 = df.apply(lambda x: x+10)
print("DataFrame after applying lambda function(+10): ")
print(df2)

df['A'] = df['A'].map(lambda A: A/2.)
print("DataFrame after applying lambda function(/2.): ")
print(df)

df2 = df.apply(lambda x: np.square(x) if x.name in ['A', 'B'] else x)
print("DataFrame after applying lambda function(square(x) if in [A or B] else x): ")
print(df2)

