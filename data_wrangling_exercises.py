# Name : Ruth Ereso

import pandas as pd
import numpy as np


# Hospital Patient Registration


data = {
'Patient_ID':['P001','P002','P003','P004','P004'],
'Full_Name':['Abebe Kebede',' Hana Tesfaye ','Samuel Bekele','Meron Alemu','Meron Alemu'],
'Age':[35,np.nan,42,29,29],
'Address':[
'Bole Road, Addis Ababa, Bole, 03, H125',
'CMC Road, Addis Ababa, Yeka, 10, H201',
'Piassa, Addis Ababa, Arada, 01, H505',
'Megenagna, Addis Ababa, Bole, 05, H901',
'Megenagna, Addis Ababa, Bole, 05, H901'
]
}

df = pd.DataFrame(data)

print(df)

print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())

df = df.drop_duplicates()

df["Full_Name"] = df["Full_Name"].str.strip()

df[["First_Name","Last_Name"]] = df["Full_Name"].str.split(" ",expand=True)

df[["Street","City","Subcity","Woreda","House_No"]] = df["Address"].str.split(",",expand=True)

print(df)


# Online Store Sales Report

data = {
'Month':['Jan','Jan','Feb','Feb','Mar','Mar'],
'Product':['Laptop','Phone','Laptop','Phone','Laptop','Phone'],
'Sales':[15,np.nan,18,20,15,25]
}

df = pd.DataFrame(data)

print(df)

print(df.isnull().sum())

df["Sales"] = df["Sales"].fillna(0)

print(df["Sales"].sum())


pivot = df.pivot_table(
    index="Month",
    columns="Product",
    values="Sales"
)

pivot = pivot.fillna(0)

print(pivot)

print(pivot.sum(axis=1).idxmax())


#  Employee Email Processing


data = {
'Employee_ID':['E1','E2','E3','E4'],
'Email':[
'abebe@gmail.com',
'hana@yahoo.com',
'samuel@outlook.com',
'meron@gmail.com'
]
}

df = pd.DataFrame(data)


df[["Username","Domain"]] = df["Email"].str.split("@",expand=True)

df["Username"] = df["Username"].str.upper()

df["Company_Email"] = df["Username"].str.lower()+"@company.com"


print(df)

print((df["Domain"]=="gmail.com").sum())

print(df[df["Domain"]=="gmail.com"])


# Bank Loan Approval


data = {
'Region':['Addis','Addis','Adama','Adama','Hawassa','Bahir Dar'],
'Loan_Type':['Personal','Mortgage','Personal','Mortgage','Personal','Mortgage'],
'Status':['Approved','Rejected','Approved','Approved','Rejected','Approved']
}

df = pd.DataFrame(data)

df["Count"] = 1


pivot = df.pivot_table(
    index="Region",
    columns=["Loan_Type","Status"],
    values="Count",
    aggfunc="sum"
)


pivot = pivot.fillna(0)

print(pivot)

print((df["Status"]=="Approved").sum())



# Telecom Customer Usage


data = {
'Customer_ID':['C1','C1','C2','C2','C1','C3'],
'Month':['Jan','Jan','Jan','Jan','Feb','Feb'],
'Service':['Data','Voice','Data','Voice','Data','Voice'],
'Usage_GB':[12,5,8,10,np.nan,15]
}

df = pd.DataFrame(data)


print(df.isnull().sum())


df["Usage_GB"] = df["Usage_GB"].fillna(df["Usage_GB"].mean())


pivot = df.pivot_table(
    index="Customer_ID",
    columns=["Month","Service"],
    values="Usage_GB"
)


pivot = pivot.fillna(0)

print(pivot)


print(pivot.sum(axis=1).idxmax())


print(df.groupby("Customer_ID")["Usage_GB"].mean())


# Product Code Cleaning



data = {
'Product_Code':[
'TV-2025-001',
'LAP-2025-017',
'PHN-2024-023',
'TAB-2025-011'
],
'Price':['45000','65000','32000','55000']
}


df = pd.DataFrame(data)


df["Price"] = df["Price"].astype(int)


df[["Category","Year","Product_Number"]] = df["Product_Code"].str.split("-",expand=True)


print(df["Price"].mean())


print(df.loc[df["Price"].idxmax()])


print(df[df["Year"]=="2025"])


print(df["Price"].sum())



#  University Student


data = {
'Student_ID':['S1','S2','S3','S3'],
'Full_Name':['Abel Bekele',' Hana Alemu ','Meron Tadesse','Meron Tadesse'],
'Department':['CS','IT',None,'IT'],
'CGPA':[3.6,3.9,3.2,3.2]
}


df = pd.DataFrame(data)


print(df.isnull().sum())


df = df.drop_duplicates()


df["Full_Name"] = df["Full_Name"].str.strip()


df[["First_Name","Last_Name"]] = df["Full_Name"].str.split(" ",expand=True)


df["Department"] = df["Department"].fillna("Unknown")


print(df.loc[df["CGPA"].idxmax()])


avg = df["CGPA"].mean()


print(avg)


print(df[df["CGPA"] > avg])


#  HR Attendance


data = {
'Employee_ID':['E1','E1','E1','E2','E2','E3','E3'],
'Month':['Jan','Jan','Feb','Jan','Feb','Jan','Feb'],
'Status':['Present','Absent','Present','Present','Present','Absent','Absent']
}


df = pd.DataFrame(data)


df["Count"] = 1


pivot = df.pivot_table(
    index="Employee_ID",
    columns=["Month","Status"],
    values="Count",
    aggfunc="sum"
)


pivot = pivot.fillna(0)


print(pivot)


absent = df[df["Status"]=="Absent"].groupby("Employee_ID")["Count"].sum()


print(absent)


print(absent.idxmax())


total = df.groupby("Employee_ID")["Count"].sum()


absence = (absent / total * 100).fillna(0)


print(absence)


print(absence.idxmin())

#  Customer Orders

data = {
'Customer_ID':['C001','C002','C003','C003'],
'Full_Name':['Abebe Kebede',' Hana Alemu ','Meron Tadesse','Meron Tadesse'],
'Address':[
'Bole Road, Addis Ababa, Bole, 03, H125',
'CMC Road, Addis Ababa, Yeka, 10, H201',
'Piassa, Addis Ababa, Arada, 01, H505',
'Piassa, Addis Ababa, Arada, 01, H505'
],
'Product':['Laptop','Phone','Laptop','Tablet'],
'Amount':[45000,np.nan,32000,28000]
}


df = pd.DataFrame(data)


print(df.isnull().sum())


df["Amount"] = df["Amount"].fillna(df["Amount"].mean())


df = df.drop_duplicates()


df["Full_Name"] = df["Full_Name"].str.strip()


df[["First_Name","Last_Name"]] = df["Full_Name"].str.split(" ",expand=True)


df[["Street","City","Subcity","Woreda","House_No"]] = df["Address"].str.split(",",expand=True)


df["Count"] = 1


pivot = df.pivot_table(
    index="Customer_ID",
    columns="Product",
    values="Count",
    aggfunc="sum"
)


print(pivot.fillna(0))


print(df.loc[df["Amount"].idxmax()])


avg = df["Amount"].mean()


print(avg)


print(df[df["Amount"] > avg])


df["Full_Address"] = (
df["Street"]+","+df["City"]+","+df["Subcity"]+","+df["Woreda"]+","+df["House_No"]
)


df = df.drop(columns=["Street","City","Subcity","Woreda","House_No"])


print(df)