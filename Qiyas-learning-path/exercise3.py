# =====================================================
# Exercise 3: Product Inventory Analyzer
# =====================================================

products = [
    ("Laptop", 15, 70000),
    ("Mouse", 50, 1200),
    ("Keyboard", 30, 2500),
    ("Monitor", 10, 15000),
    ("USB", 100, 500)
]


def total_inventory_value(product_list):
    """
    Calculate total inventory value.
    quantity * price
    """
    return list(map(lambda p: (p[0] , p[1] * p[2]), product_list))



def most_expensive_product(product_list):
    """
    Return most expensive product.
    """
    return max(p[2] for p in product_list)


def low_stock_products(product_list):
    """
    Return products with quantity < 20.
    """
    return list(filter(lambda p: p[1] < 20, product_list))


def increase_prices(product_list):
    """
    Increase prices by 15% using map().
    """
    return list(map(lambda p:(p[0], p[1], p[2] + p[2] * 0.15), product_list))


def sort_products_by_quantity(product_list):
    """
    Sort products by quantity.
    """
    return sorted(product_list,  key = lambda p:p[1] )


def process_quantities(product_list):
    """
    Square even quantities.
    Cube odd quantities.
    """
    result = [p[1] ** 3 if p[1] % 2 else p[1] ** 2 for p in product_list]
    return result
# result2 = [value ** 3 if value % 2 else value ** 2 for value in data2]


def expensive_products(product_list):
    """
    Use filter() to get products costing above 5000.
    """
    return list(filter(lambda p: p[2] > 5000, product_list))
   


print("total_inventory_value", total_inventory_value(products))
print("most_expensive_product", most_expensive_product(products))
print("low_stock_products", low_stock_products(products))
print("increase_prices", increase_prices(products))
print("sort_products_by_quantity", sort_products_by_quantity(products))
print("expensive_products",expensive_products(products))
print("process_quantities", process_quantities(products))
