import pandas as pd
df = pd.read_csv("stock_data.csv")
df.to_csv("temp.csv", columns=["tickers", "people"], index=True)

temp = pd.read_csv("temp.csv")
temp = temp.tail(3)
temp.to_csv("2columns_3rows.csv", index=True)
