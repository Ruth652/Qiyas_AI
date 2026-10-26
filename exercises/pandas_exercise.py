import pandas as pd

# # dataframe from list
# courses = ["python", "Java", "SQL"]

# df = pd.DataFrame(courses)
# print(df)

# # dataframe from dictionary

# data = {
#     "Name":["RuthG", "Yeabsira"],
#     "Age":[21, 22]
# }
# df = pd.DataFrame(data)
# print(df)

# student_data = {
#     "Name":["RuthE", "GreenH",],
#     "Department":["IS", "CS"],
#     "Year":[4, 3]
# }

# df = pd.DataFrame(student_data)

# employee_data = {
#     "Name":["Sara", "Jhon", "Mike"],
#     "Salary":[50000 , 60000, 55000],
# }

# df = pd.DataFrame(data)
# print(df)

# data = {
#     "Name":["Abel", "Hana", "Robel"]
#   
# }
# df = pd.DataFrame(data, index = ["s1", "s2", "s3"])
# print(df)

# select one column, select Multiple columns
employee_data = {
    "Name":["Sara", "Jhon", "Mike"],
    "Department":["IS", "CS", "SE"]
}

df = pd.DataFrame(employee_data)
# print(df["Name"])
# print(df[["Name", "Department"]])

# # Add new column
# df["CGPA"] = [3.5, 3.4, 3.3]
# print(df)

# # rename column
# df.rename(columns = 
# {"Department": "Major"},
# inplace = True
# )
# print(df)

# # Delete column

# df.drop("CGPA", axis = 1,
#         inplace = True
# )
# print(df)

# using loc[]
# df.index = [101, 102, 103]
# print(df.loc[102])
# print(df.loc[102, "Name"])

# # using iloc[]
# print("second row",df.iloc[1])

# # first two rows
# print(df.iloc[:2])
# # first row and first column
# print(df.iloc[0, 0])

# student_data = {
#     "Name":["Abel","Hana", "Robel"],
#     "Math":[80, 90, 70]
# }

# df = pd.DataFrame(student_data)
# print("Average mark", df["Math"].mean())
# print("Maximum mark", df["Math"].max())
# print("Lowest mark", df["Math"].min())
# print("Total mark", df["Math"].sum())
# print("higher than 80", df[df["Math"] > 80])


data = {
    "course":
    ["CS", "IT", "SE", "DS"],
    "students":
    [100, 200, 150, 300]
}

df = pd.DataFrame(data)
print(df["students"].sum())
# top enrolled course
print(df.loc[df["students"].idxmax()])


# mini projects
data = {
    "Name": ["Abel", "Hana", "Robel", "Ruth"],
    "Math": [80, 90, 70, 85],
    "Physics": [85, 95, 75, 90],
    "Chemistry": [78, 88, 68, 82]
}

df = pd.DataFrame(data)

df["Total"] = (
    df["Math"] + df["Physics"] + df["Chemistry"]
)

df["Average"] = df["Total"] / 3
print(df)

top_student = df.sort_values(by = "Average", ascending = False)

print(top_student)


