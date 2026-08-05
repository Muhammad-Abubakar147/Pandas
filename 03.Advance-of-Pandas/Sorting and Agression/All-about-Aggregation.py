import pandas as pd

data = {
    "Name": ["Omer", "Zabiullah", "Hassan"],
    "Salary": [28500, 56778, 64779]
}

df = pd.DataFrame(data)

print("Total Salary:", df["Salary"].sum())
print("Average Salary:", df["Salary"].mean())
print("Maximum Salary:", df["Salary"].max())
print("Minimum Salary:", df["Salary"].min())
print("Number of Employees:", df["Salary"].count())