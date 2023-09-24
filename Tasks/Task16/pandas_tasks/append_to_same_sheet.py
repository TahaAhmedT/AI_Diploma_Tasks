import pandas as pd


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

new.to_excel("test.xlsx", mode='a', index=True)
