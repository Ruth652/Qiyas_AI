import pandas as pd
import numpy as np

data = {
    "Name": ["Abel", "Sara", "Hana"],
    "Age": [22, 21, 20]
}

df = pd.DataFrame(data)
print(df)

departments = ["CS", "IT", "SE", "DS"]
df = pd.DataFrame(departments)

print(df)


students = {
    "Name": ["Abel", "Sara", "Hana", "David", "Marta"],
    "Age": [22, 21, 20, 23, 22],
    "GPA":[3.5, 3.8, 3.9, 3.2, 3.7],
}

df = pd.DataFrame(students)
print("shape", df.shape)
print("columns", df.columns)
print("data types", df.dtypes)
print("display the first 3 rows", df.head(3))
print("display the last 2 rows",df.tail(2))


print("display the name colum", df["Name"])
print("display the Name and GPA column", df[["Name", "GPA"]])
print("display the first row using loc", df.loc[0])
print("display the first row using iloc", df.iloc[0])
print("display the first row using head", df.head(1))
print("display sara's gpa", df.loc[1, "GPA"]) # df.loc[1, 2]
print("display hana's gpa", df.iloc[2, 1])
print("display students older than 21", df[df["Age"] > 21])
print("Display students older than 20 and GPA above 3.5", df[(df["Age"] > 20) & (df["GPA"] > 3.5)])

# creating a precentage column
df["Percentage"] = df["GPA"] * 25
print("display the dataframe with percentage column", df)
df["Pass"] = df["GPA"].apply(
    lambda x: "Pass" if x >= 2.0 else "Fail"
)
print("find average Age", df["Age"].mean())
print( "find the highest GPA", df["GPA"].max())
print("find the lowest GPA", df["GPA"].min())
print("find the total age", df["Age"].sum())

print("number of students", df["Name"].count())
print("find number of students with GPA above 3.5", df[df["GPA"] > 3.5]["Name"].count())
print("sorting gpa in ascending order", df.sort_values("GPA"))
print("sort gpa in descending order", df.sort_values("GPA", ascending = False))


# missing Data
data = {
    "Name": ["Abel", "Sara", None, "David", "Marta"],
    "Age": [22, 21, 20, np.nan, 22],
    "GPA":[3.5, 3.8, 3.9, 3.2, 3.7],
}

df = pd.DataFrame(data)
print(df)
print("check missing values", df.isnull())
print("count missing values per column ", df.isnull().sum())
print("count missing values in the entire dataFrame",df.isnull().sum().sum())
print("Replace missing values with 0", df.fillna(0))
df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)

print("replaced missing value of age by mean",df)
print("Remove rows containing missing values" , df.dropna())

print("Print all student names using iterrows")
for index, row in df.iterrows():
    print(row["Name"])

print("print all student names using itertuples")
for row in df.itertuples():
    print(row.Name)

df["Scholarship"] = df["GPA"].apply(
    lambda x: "Full" if x >= 3.7 else "Partial" if x >= 3.3 else "None"
)

'''
def scholarship(gpa):

    if gpa >= 3.7:
        return "Full"
    elif gpa >= 3.3:
        return "Partial"
    return "None"
df["Scholarship"] = df["GPA"].apply(scholarship)
'''

df["Classification"] = df["GPA"].apply(
    lambda x: "Distinction" if x >= 3.7 else "Very Good" if x >= 3.0 else "Probation"
)