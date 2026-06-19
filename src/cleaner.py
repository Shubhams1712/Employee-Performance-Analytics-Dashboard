import pandas as pd

def clean_data(df):
    df = df.drop_duplicates().copy()

    df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
    df["Department"] = df["Department"].replace({
        "Hr": "HR",
        "sales": "Sales",
        "Finanace": "Finance",
        "Marketng": "Marketing"
    })
    df["Rating"] = df["Rating"].fillna(df["Rating"].mean())

    condition1 = df["Working_Hours"] <= 0
    condition2 = df["Salary"] <= 0
    condition3 = df["Rating"] <= 0
    condition4 = df["Rating"] > 5
    indication = condition1 | condition2 | condition3 | condition4
    df = df[~indication].copy()

    return df
