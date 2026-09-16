# ============================================================
# PYTHON FUNDAMENTALS - 18_TYPE_CONVERSION
# ============================================================

# String to integer

age = "30"
age_number = int(age)

print(age_number)
print(type(age_number))

# String to float

price = "99.50"
price_number = float(price)

print(price_number)

# Integer to string

number = 100
text = str(number)

print(text)
print(type(text))

# Integer to float

number = 10
decimal = float(number)

print(decimal)

# Float to integer

price = 99.99
price_int = int(price)

print(price_int)

# List to set

items = ["Python", "Python", "SQL"]
unique_items = set(items)

print(unique_items)

# Set to list

items_list = list(unique_items)

print(items_list)

# Boolean conversion

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))

# Practical API example

customer_id = "1001"

customer_id = int(customer_id)

print("Customer ID:", customer_id)
print("Type:", type(customer_id))
