import pandas as pd

customers = pd.DataFrame({
    "Customer_ID": ["C001", "C002", "C003", "C005", "C006"],
    "Customer_Name": ["Abel", "Sara", "John", "Helen", "Samuel"],
    "City": ["Addis Ababa", "Adama", "Jimma", "Bahir Dar", "Hawassa"]
})
orders = pd.DataFrame({
"Order_ID":[101,102,103,104,105,106],
"Customer_ID":["C001","C002","C003","C001","C004","C006"],
"Product":["Laptop","Phone","Keyboard","Mouse","Monitor","Tablet"],
"Amount":[1200,800,150,45,400,700]
})

employees = pd.DataFrame({
"Employee_ID":[1,2,3,4,5,6],
"Department":["IT","IT","Sales","Sales","HR","HR"],
"Employee":["Abel","Sara","John","Helen","Samuel","David"],
"Salary":[5000,6500,4500,4700,5200,4900]
})

result = pd.merge(
    orders,
    customers,
    on = "Customer_ID",
    how="inner"
)

print("inner join: ",result)
print("rows returned:", len(result))

missing_customers = set(orders["Customer_ID"]) - set(customers["Customer_ID"])
print("Missing customers:", missing_customers)

1
result = pd.merge(
    orders,
    customers,
    on = "Customer_ID",
    how = "left"
)

print("left join: ",result)
missing_customers = result[result["Customer_Name"].isnull()]["Customer_ID"]
print("Missing customers:", missing_customers)
print("replaced missing values with unknown", result.fillna("Unknown", inplace=True))


result = pd.merge(
    orders,
    customers,
    on = "Customer_ID",
    how= "right"
)

print("right join: ",result)
customer_without_orders = result[result["Order_ID"].isnull()]["Customer_ID"]
print("Customers without orders:", customer_without_orders)
print("values contained NaN:", result.isnull().sum())


print("products with amount > 500", orders[orders["Amount"] > 500]["Product"])
print("order with product is either phone or laptop: ", orders[orders["Product"].isin(["Laptop", "Phone"])])
# print(orders[
#     (orders["Product"] == "Laptop") | (orders["Product"] == "Phone")
# ])
print("amount is between 200 and 900", orders[(orders["Amount"] >= 200) & (orders["Amount"] <= 900)])
print("Display customers only from addis ababa and hawassa: ",customers[customers["City"].isin(["Addis Ababa", "Hawassa"])])
print("customers whose name starts with 'S': ", customers[customers["Customer_Name"].str.startswith("S")])
print("Display all products except Mouse: ", orders[orders["Product"] != "Mouse"])

print("total sales amount: ", orders["Amount"].sum())
print("average sales amount: ", orders["Amount"].mean())
print("maximum sales amount: ", orders["Amount"].max())
print("minimun sales amount: ", orders["Amount"].min())
print("total number of orders: ", len(orders))



result = pd.merge(
    orders,
    customers,
    on = "Customer_ID",
    how="inner"
)
print("inner join: ",result)
print("cities with the least order :",result.groupby("City")["Order_ID"].count().idxmin()) 
print("Cities with the least order amount:", result.groupby("City")["Amount"].sum().idxmin())

print("total salary: ", employees["Salary"].sum())
print("total salary for each department: ", employees.groupby("Department")["Salary"].sum())
print(employees.groupby("Department")["Salary"].mean())

result = pd.merge(
    orders,
    customers,
    on = "Customer_ID",
    how="outer"
)

print("outer join total rows: ", len(result))
print("outer join: ",result)
customer_in_onedataset = result[result["Customer_Name"].isnull()|result["Order_ID"].isnull()]["Customer_ID"]
print("customer in one dataset: ", customer_in_onedataset)


print("count of Employees in each department: ", employees.groupby("Department")["Employee"].count())
print(employees["Salary"].agg(["mean", "max", "min", "count"]))
employees["Bonus"] = employees["Salary"] * 0.1
employees["Tax"] = employees["Salary"] * 0.15
employees["Net_salary"] = employees["Salary"]  - employees["Tax"]

print("new rows added: ", employees)
# def salary_level(Salary):
#     if Salary >= 6000:
#         return "High"
#     elif Salary >= 5000 and Salary < 6000:
#         return "Medium"
#     else:
#         return "Low"
# employees["Level"] = employees["Salary"].apply(salary_level)


employees["Level"] = employees["Salary"].apply(
    lambda x: "High" if x >= 6000 else ("Medium" if x >= 5000 else "Low")
)
print("new column added: ", employees)

employees["Department_type"] = employees["Department"].apply(
    lambda x: "Technical" if x == "IT" else "Non-Technical"
)
print("new column added: ", employees)

merged_= pd.merge(
    orders,
    customers,
    on = "Customer_ID",
    how="outer"
)


print(merged_[["Customer_Name", "Product", "Amount"]].sort_values("Amount", ascending=False))
print("customer who spent the most money: ", merged_.groupby("Customer_Name")["Amount"].sum().idxmax())
print("total amount spent by each customer: ", merged_.groupby("Customer_Name")["Amount"].sum().sort_values(ascending=False))
total = merged_.groupby("Customer_Name")["Amount"].sum()
result = total[total > 1000]
print("Customers whose total purchases exceed 1000:\n", result)

# result = (
#     merged_
#     .groupby("Customer_Name")["Amount"]
#     .sum()
#     .loc[lambda x: x > 1000]
# )

# print(result)pip install seaborn scikit-learn scipy jupyter
