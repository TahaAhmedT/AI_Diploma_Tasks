import pandas as pd

df = pd.read_excel("test.xlsx", "Sheet1")
print(df)
print()


def convert_people_cell(cell):
    if cell == "n.a.":
        return 'data not available'
    return cell


def convert_price_cell(cell):
    if cell == "n.a.":
        return 14.8
    return cell


def convert_eps_cell(cell):
    if cell == "not available":
        return 18.36
    return cell


new = pd.read_excel("test.xlsx", "Sheet1", converters={
    'people': convert_people_cell,
    'price': convert_price_cell,
    'eps': convert_eps_cell
})

df = df._append(new, ignore_index=True)
print(df)
df.to_excel("test.xlsx", index=True, sheet_name="Sheet1")
