# Name = Ruth Ereso

import pandas as pd
import numpy as np

university = pd.DataFrame({
"student_id":[201,202,203,204,205,206,207,208,209,210],
"name":
["Abel","Sara",None,"John","Marta",None,"David","Helen","Tom",None],
"department":["CS","IT","CS",None,"SE","IT","SE",None,"CS","IT"],
"gpa":[3.5,3.8,np.nan,2.9,3.7,np.nan,3.2,3.4,3.9,np.nan],
"scholarship":
[5000,np.nan,3000,2000,np.nan,4000,3500,np.nan,5000,np.nan]
})


# Data cleaning
print("count missing values per column", university.isnull().sum())
print("count total missing values", university.isnull().sum().sum())
print("Missing value percentage", university.isnull().sum() / len(university) * 100)
print("replace missing name with unkown", university["name"].fillna("Unknown"))
print("replace missing gpa with median", university["gpa"].fillna(university["gpa"].median()))
print("replace missing gpa with mode", university["gpa"].fillna(university["gpa"].mode()[0]))
print("replace missing scholarship with zero", university["scholarship"].fillna(0))

# Data analytics
print("Number of students by department", university.groupby("department")["student_id"].count())
print("Number of scholarship reciepients", university[university["scholarship"] > 0]["student_id"].count())
print("The highest GPA", university["gpa"].max())
print("The lowest GPA", university["gpa"].min())
print("Total scholarship amount", university["scholarship"].sum())



