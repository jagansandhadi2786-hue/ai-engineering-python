# ============================================================
# PYTHON FUNDAMENTALS - 03_INPUT
# ============================================================
# Topics:
# 03 - INPUT
#
# Practice:
# - User input
# - String input
# - Integer input
# - Float input
# ============================================================
# TOPIC 03 - INPUT()
# ============================================================

print("\n" + "=" * 60)
print("TOPIC 03 - INPUT()")
print("=" * 60)


# ------------------------------------------------------------
# Exercise 1 - Get user's name
# ------------------------------------------------------------

name = input("Enter your name: ")

print("Hello", name)


# ------------------------------------------------------------
# Exercise 2 - Get user's city
# ------------------------------------------------------------

city = input("Enter your city: ")

print("You live in", city)


# ------------------------------------------------------------
# Exercise 3 - Get age
# ------------------------------------------------------------

age = int(input("Enter your age: "))

print("Your age is:", age)


# ------------------------------------------------------------
# Exercise 4 - Get salary
# ------------------------------------------------------------

salary = float(input("Enter your salary: "))

print("Your salary is:", salary)


# ------------------------------------------------------------
# Exercise 5 - Personal information
# ------------------------------------------------------------

print("\n--- Personal Information ---")

name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")
country = input("Country: ")

print("\nYour Information")
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Country:", country)


# ============================================================
# END OF PRACTICE FILE
# ============================================================

print("\n" + "=" * 60)
print("TOPIC 03 PRACTICE COMPLETED")
print("=" * 60)