import pandas as pd
import numpy as np

students = pd.DataFrame({
"student_id":[101,102,103,104,105,106,107,108,109,110],
"name":
["Abel","Sara",None,"John","Marta",None,"David","Helen","Tom",None],
"department":["CS","IT","CS",None,"SE","IT","SE",None,"CS","IT"],
"gpa":[3.5,3.8,np.nan,2.9,3.7,np.nan,3.2,3.4,3.9,np.nan],
"scholarship":
[5000,np.nan,3000,2000,np.nan,4000,3500,np.nan,5000,np.nan]
})

print("all missing values in the dataset", students.isnull())
print("count missing values in each column", students.isnull().sum())
# the first sum counts missing value per column, the 2nd sum counts the total number of missing values in the dataset
print("count the total number of missing values in the dataset", students.isnull().sum().sum())

# This helps to determine which column should be cleaned, imputed, or removed
print("the percentage of missing values in each column", 
      (students.isnull().sum() / len(students)) * 100)

print("check", students.isnull().any())
print("displaying only columns names that contain missing values", 
      students.columns[students.isnull().any()])

# usefull when reviewing incomplete records
print("displaying only rows that contain missing values",
    students[students.isnull().any(axis = 1)]
)
print("student whose GPA is missing", students[students["gpa"].isnull()])
print("student whose scholarship is missing", students[students["scholarship"].isnull()])

# common approach for categorical attributes
print("replace missing names with unknown", students["name"].fillna("Unknown"))
print("replace missing GPA using the mean", 
    students["gpa"].fillna(students["gpa"].mean())
)


# Median is often preferred when outliers exist
print("replace missing GPA using the median",
    students["gpa"].fillna(students["gpa"].median())
)

# mode is typically used for categorical columns
print("replace missing department with the most common department",
    students["department"].fillna(students["department"].mode()[0])
)
print("replace missing scholarship values with zero", students["scholarship"].fillna(0))
print("remove rows containing missing values", students.dropna())
print("remoce columns containing missing values", students.dropna(axis = 1))
students["gpa_missing"] = students["gpa"].isnull()
print("create a gpa missing value flag", students)
students["scholarship_missing"] = students["scholarship"].isnull()
print("create a scholarship missing value flag", students)
print("find the column with the highest number of missing values", students.isnull().sum().idxmax())
print("find the column with the lowest number of missing values", students.isnull().sum().idxmin())
print("find the dataset completeness precentage", 100 - 
(
    students.isnull().sum().sum() / students.size
) * 100)