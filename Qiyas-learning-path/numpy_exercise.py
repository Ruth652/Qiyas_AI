import numpy as np

# =====================================================
# TASK 1: SALES DATA SLICING
# =====================================================

sales = np.array([
    [120, 150, 180],
    [200, 220, 210],
    [170, 160, 190]
])

'''
Columns represent:
Morning
Afternoon
Evening

Rows represent:
Monday
Tuesday
Wednesday
'''

print("Tuesday afternoon:", sales[1, 1])
print("Morning sales:", sales[:, 0])
print("Evening sales:", sales[:, 2])
print("Monday sales:", sales[0, :])
print("Tuesday and Wednesday sales:", sales[1:, :])
print("Afternoon and evening sales for all days:", sales[:, 1:])

print("\n" + "=" * 50 + "\n")

# =====================================================
# TASK 2: STUDENT SCORES
# =====================================================

scores = np.array([
    [80, 75, 90],
    [65, 70, 60],
    [95, 88, 92],
    [72, 78, 85]
])

'''
Columns:
Math
Physics
Chemistry

Rows:
Abel
Sara
John
Helen
'''

print("Sara's Physics score:", scores[1, 1])
print("Math scores:", scores[:, 0])
print("Chemistry scores:", scores[:, 2])
print("John's full scores:", scores[2, :])
print("First 2 students:", scores[:2, :])
print("Physics and Chemistry scores for all students:", scores[:, 1:])

print("\n" + "=" * 50 + "\n")

# =====================================================
# TASK 3: PRODUCT SALES
# =====================================================

sales = np.array([
    [120, 130, 125, 140, 150],  # Coffee
    [200, 210, 190, 220, 230],  # Milk
    [90, 85, 95, 100, 110],     # Bread
    [60, 70, 65, 80, 75]        # Sugar
])

products = ["Coffee", "Milk", "Bread", "Sugar"]

print("Full sales data:\n")
print(sales)

print("\nSales of Product B (Milk):")
print(sales[1, :])

print("\nSales for Day 3 (all products):")
print(sales[:, 2])

print("\nLast 2 days sales for all products:")
print(sales[:, 3:])

print("\n" + "=" * 50 + "\n")

# =====================================================
# PART 2: PRODUCT PERFORMANCE
# =====================================================

# Total sales per product

print("Total Sales Per Product")

total_sales = np.sum(sales, axis=1)

for product, total in zip(products, total_sales):
    print(product, ":", total)

highest_product = products[np.argmax(total_sales)]
print("\nHighest selling product:", highest_product)

print("\nAverage Daily Sales Per Product")

average_sales = np.mean(sales, axis=1)

for product, avg in zip(products, average_sales):
    print(product, ":", avg)

print("\nHighest Single-Day Sale")

highest_sale = np.max(sales, axis=1)

for product, sale in zip(products, highest_sale):
    print(product, ":", sale)

print("\nLowest Single-Day Sale")

lowest_sale = np.min(sales, axis=1)

for product, sale in zip(products, lowest_sale):
    print(product, ":", sale)

print("\n" + "=" * 50 + "\n")

# =====================================================
# PART 3: DAILY ANALYSIS
# =====================================================

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

print("Total Sales Per Day")

total_sale_day = np.sum(sales, axis=0)

for day, sale in zip(days, total_sale_day):
    print(day, ":", sale)

highest_sale_day = days[np.argmax(total_sale_day)]

print("\nHighest Sales Day:", highest_sale_day)

print("\nAverage Sales Per Day")

avg_sale_day = np.mean(sales, axis=0)

for day, sale in zip(days, avg_sale_day):
    print(day, ":", sale)

print("\n" + "=" * 50 + "\n")

# =====================================================
# PART 4: BUSINESS INSIGHTS
# =====================================================

product_sales = np.sum(sales, axis=1)

best_selling = products[np.argmax(product_sales)]
worst_selling = products[np.argmin(product_sales)]

print("Best Selling Product:", best_selling)
print("Worst Selling Product:", worst_selling)
print("Best Performing Day:", highest_sale_day)

print("\n" + "=" * 50 + "\n")

# =====================================================
# PART 5: FILTERING & BUSINESS RULES
# =====================================================

print("Products with any day sales > 200")

result = np.any(sales > 200, axis=1)

for product, found in zip(products, result):
    if found:
        print(product)

print("\nProducts that never crossed 100 units")

result2 = np.all(sales <= 100, axis=1)

for product, found in zip(products, result2):
    if found:
        print(product)

print("\nDays where total store sales exceeded 500")

total_sale_daily = np.sum(sales, axis=0)

result3 = total_sale_daily > 500

for day, found in zip(days, result3):
    if found:
        print(day)

















