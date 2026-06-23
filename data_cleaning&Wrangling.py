import pandas as pd
import numpy as np

df = pd.DataFrame({
    "student_id": [101, 102, 103, 102, 104, 101],
    "name": ["Abel", "Sara", "John", "Sara", "Helen", "Abel"],
    "score": [80, 90, 75, 90, 88, 80]
})

print("duplicated rows:", df.duplicated())
print("duplicate count:", df.duplicated().sum())
df_clean = df.drop_duplicates()
df_last = df.drop_duplicates(keep = "last")

print("cleaned:", df_clean)
print(df_last)


df = pd.DataFrame({
    "id":[1,2,3,4],
    "email":[
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com",
    "c@gmail.com"
    ]
})

duplicates = df[df.duplicated(subset=["email"])]
print(duplicates)

clean_df = df.drop_duplicates(subset=["email"])
print(clean_df)

df = pd.DataFrame({
    "city":[
    "addis ababa",
    "ADDIS ABABA",
    "Addis Ababa",
    "adDis abAba"
    ]
})

df["upper"] = df["city"].str.upper()
df["lower"] = df["city"].str.lower()
df["title"] = df["city"].str.title()
print(df)


df = pd.DataFrame({
"name":[
" Abel",
"Sara ",
" John ",
" Helen"
]
})

# remove extra spaces
df["name"] = df["name"].str.strip()
print(df)
df = pd.DataFrame({
    "date":[
    "2026-01-05",
    "05/02/2026",
    "March 10, 2026",
    "2026.04.15"
    ]
})

# Standardize Dates
df["date"] = pd.to_datetime(df["date"], format="mixed")

df["formatted"] = df["date"].dt.strftime("%Y-%m-%d")
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

print(df)

df = pd.DataFrame({
"weight_kg":[55,70,85,100]
})
# kilograms to pounds
df["weight_lb"] = (df["weight_kg"] * 2.20462).round(2)
print(df)

df = pd.DataFrame({
    "temp_c": [0, 25, 37, 100]
})

df = pd.DataFrame({
    "temp_c":[0, 25, 37, 100]
})

# Convert Celsius to Fahrenheit.
df["temp_f"] = (df["temp_c"] * 9/5) + 32
print(df)


df = pd.DataFrame({
"name":["Abel","Sara",None,"John"],
"age":[20,np.nan,25,30]
})

print(df.isnull())
print(df.isnull().sum())
df["age"] = df["age"].fillna(df["age"].mean())
df["name"] = df["name"].fillna("Unknown")
print(df)

df = pd.DataFrame({
"gender":[
"Male",
"male",
"MALE",
"Female",
"female"
]
})

df["gender"] = df["gender"].str.title()
print(df)

df = pd.DataFrame({
"salary_usd":[
500,800, 1200, 1500
]
})

'''
convert USD to ETB
'''

exchange_rate = 135
df["salary_etb"] = df["salary_usd"] * exchange_rate
print(df)

df = pd.DataFrame({
"salary":[
3500,4000, 1200, 1500
]
})


q1 = df["salary"].quantile(0.25)
q3 = df["salary"].quantile(0.75)

# ? 
IQR = q3 - q1
lower = q1 - 1.5 * IQR
upper = q3 + 1.5 * IQR

outliers = df[
    (df["salary"] < lower) |
    (df["salary"] > upper)
]

print(outliers)

clean_df = df[
     (df["salary"] >= lower) & 
      (df["salary"] <= upper)
]

print(clean_df)

df = pd.DataFrame({
"phone":[
"0922646696","+251922646696", "251922646696", "0922-646-696"
]
})

'''
Remove symboles
convert all numbers to +251 format
'''

df["phone"] = df["phone"].str.replace("-", "", regex = False)
df["phone"]  = df["phone"].str.replace("+", "", regex=False)

df["phone"] = df["phone"].apply(
    lambda x:
    "+251" + x[1:]
    if x.startswith("0")
    else "+251" + x[3:]
)

print(df)

df = pd.DataFrame({
"email":[
"ABEL@GMAIL.COM","+sara@gmail.com", "JOHN@YAHOO.COM"
]
})
'''
 remove spaces
 convert to lowercase
 validate emails
'''

df["email"] = df["email"].str.strip()
df["email"] = df["email"].str.lower()
df["valid"] = df["email"].str.contains("@")

print(df)


df = pd.DataFrame({
"product":[
"Laptop","laptop", "LAPTOP", "Laptop"
]
})


'''
 standardize product names
compare unique counts before and after cleaning
'''

print("Before:", df["product"].nunique())

df["product"] = (
    df["product"]
    .str.strip()
    .str.lower()
)

print("After:", df["product"].nunique())
print(df)


df = pd.DataFrame({
"name":[" Abel ","Sara",None,"JOHN"],
"age":[20,np.nan,25,30],
"salary":[4000,4500,5000,45000],
"join_date":[
"2026-01-01",
"01/02/2026",
"March 10, 2026",
"2026.04.15"
]
})

'''
1. Clean names.
2. Fill missing values.
3. Standardize dates.
4. Detect outliers.
'''


df["age"] = df["age"].fillna(df["age"].mean())
df["join_date"] = pd.to_datetime(df["join_date"], format="mixed")

Q1 = df["salary"].quantile(0.25)
q3 = df["salary"].quantile(0.75)

IQR = q3 - q1

lower = q1 - 1.5 * IQR
upper = q3 + 1.5 * IQR

outliers = df[
    (df["salary"] < lower ) |
    (df["salary"] > upper)
]

print(df)
print("outliers")
print(outliers)