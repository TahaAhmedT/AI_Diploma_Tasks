import pandas as pd

df = pd.DataFrame({'col2': [150, 140, 170],
                   'col1': [70, 20, 30]},
                  index=[3, 2, 1])

print("DataFrame before Sorting: ")
print(df)
print()

sorted_df = df.sort_index(axis=0, kind='mergesort')
print("DataFrame after Sorting by index: ")
print(sorted_df)
print()

sorted_df = df.sort_index(axis=1)
print("DataFrame after Sorting by columns: ")
print(sorted_df)
