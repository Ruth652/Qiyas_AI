import pandas as pd

students = {
    "StudentID": [1,2,3,4,5],
    "Name":["Abel", "Sara", "Hana", "David", "Marta"],
    "Department":["CS", "IT", "SE", "DS", "CS"],
    "Age":[22, 21, 20, 23, 22],
    "GPA":[3.5, 3.8, 3.9, 3.2, 3.7],
}
df = pd.DataFrame(students)

print("Average GPA")
print(df["GPA"].mean())


print("\nHighest GPA")
print(df["GPA"].max())

print("\nLowest GPA")
print(df["GPA"].min())


df["Percentage"] = df["GPA"] * 25

df["Classification"] = df["GPA"].apply(
    lambda gpa : "Distinction" if gpa >= 3.7
    else "Very Good" if gpa >= 3.0
    else "Good"
)

print(df.sort_values(
    "GPA",
    ascending = False
))