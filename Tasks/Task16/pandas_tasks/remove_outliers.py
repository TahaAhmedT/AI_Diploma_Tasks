import pandas as pd
import numpy as np

# Create a sample dataset
data = {
    'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 20],
    'col2': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}

df = pd.DataFrame(data)

# Detect outliers using Z-Score method
z_scores = np.abs((df - df.mean()) / df.std())
outliers_zscore = df[z_scores > 3]

# Detect outliers using IQR method
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
outliers_iqr = df[(df < Q1 - 1.5 * IQR) | (df > Q3 + 1.5 * IQR)]

# Remove outliers from the DataFrame
df_clean_zscore = df[~((df - df.mean()) / df.std()).abs().gt(3).any(axis=1)]
df_clean_iqr = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

# Print the cleaned DataFrames
print("DataFrame after outlier removal using Z-Score method:")
print(df_clean_zscore)

print("\nDataFrame after outlier removal using IQR method:")
print(df_clean_iqr)