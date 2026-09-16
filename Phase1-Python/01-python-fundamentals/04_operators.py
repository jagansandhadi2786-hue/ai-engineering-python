# ============================================================
# PYTHON FUNDAMENTALS - 04_OPERATORS
# ============================================================
#Topics:04 - Operators
#
# Practice:
# - Arithmetic operators
# - Comparison operators
# - Logical operators
# - Assignment operators
# - Membership operators
# - Identity operators
# - Practical mini exercises
# - Final challenge
# ============================================================

# ------------------------------------------------------------
# Exercise 6 - Add two numbers
# ------------------------------------------------------------

print("\n--- Addition ---")

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

result = number1 + number2

print("Result:", result)

# ------------------------------------------------------------
# Exercise 7 - Calculate total price
# ------------------------------------------------------------

print("\n--- Total Price ---")

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Total price:", total)

# ------------------------------------------------------------
# Exercise 8 - Calculate age next year
# ------------------------------------------------------------

print("\n--- Age Next Year ---")

current_age = int(input("Enter your current age: "))

next_year_age = current_age + 1

print("Next year you will be:", next_year_age)

# ------------------------------------------------------------
# Exercise 9 - User profile
# ------------------------------------------------------------

print("\n--- User Profile ---")

user_name = input("Enter name: ")
user_role = input("Enter current role: ")
target_role = input("Enter target role: ")

print("\nProfile")
print("Name:", user_name)
print("Current Role:", user_role)
print("Target Role:", target_role)

# ------------------------------------------------------------
# Exercise 10 - Convert string input to numbers
# ------------------------------------------------------------

print("\n--- String to Number Conversion ---")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

num1 = int(num1)
num2 = int(num2)

print("Sum:", num1 + num2)


# ============================================================
# TOPIC 04 - OPERATORS
# ============================================================

print("\n" + "=" * 60)
print("TOPIC 04 - OPERATORS")
print("=" * 60)

# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================

print("\n--- 1. Arithmetic Operators ---")

a = 20
b = 6

print("a =", a)
print("b =", b)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# ------------------------------------------------------------
# Exercise 11 - Calculator
# ------------------------------------------------------------

print("\n--- Exercise 11: Calculator ---")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
    print("Modulus:", a % b)
else:
    print("Cannot divide by zero")

# ============================================================
# 2. COMPARISON OPERATORS
# ============================================================

print("\n--- 2. Comparison Operators ---")

x = 10
y = 20

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# ------------------------------------------------------------
# Exercise 12 - Age comparison
# ------------------------------------------------------------

print("\n--- Exercise 12: Age Comparison ---")

age = int(input("Enter your age: "))

print("Age is 18 or above:", age >= 18)
print("Age is below 18:", age < 18)


# ------------------------------------------------------------
# Exercise 13 - Password length
# ------------------------------------------------------------

print("\n--- Exercise 13: Password Length ---")

password = input("Enter password: ")

print("Password length:", len(password))
print("Password has 8+ characters:", len(password) >= 8)

# ============================================================
# 3. LOGICAL OPERATORS
# ============================================================

print("\n--- 3. Logical Operators ---")

age = 30
experience = 6

print("Age >= 18 AND experience >= 2:",
      age >= 18 and experience >= 2)

print("Age >= 18 OR experience >= 10:",
      age >= 18 or experience >= 10)

print("NOT age < 18:",
      not age < 18)


# ------------------------------------------------------------
# Exercise 14 - Job eligibility
# ------------------------------------------------------------

print("\n--- Exercise 14: Job Eligibility ---")

age = int(input("Enter age: "))
experience = int(input("Enter years of experience: "))

eligible = age >= 18 and experience >= 2

print("Eligible for job:", eligible)


# ------------------------------------------------------------
# Exercise 15 - AI Engineer eligibility
# ------------------------------------------------------------

print("\n--- Exercise 15: AI Engineer Eligibility ---")

python_years = float(input("Years of Python experience: "))
api_knowledge = input("Do you know REST APIs? (yes/no): ")

eligible = python_years >= 1 and api_knowledge == "yes"

print("Ready for AI Engineer learning path:", eligible)


# ============================================================
# 4. ASSIGNMENT OPERATORS
# ============================================================

print("\n--- 4. Assignment Operators ---")

number = 10

print("Starting number:", number)

number += 5
print("After += 5:", number)

number -= 3
print("After -= 3:", number)

number *= 2
print("After *= 2:", number)

number /= 4
print("After /= 4:", number)


# ------------------------------------------------------------
# Exercise 16 - Update account balance
# ------------------------------------------------------------

print("\n--- Exercise 16: Account Balance ---")

balance = 1000

deposit = float(input("Enter deposit amount: "))

balance += deposit

print("Updated balance:", balance)


# ------------------------------------------------------------
# Exercise 17 - Shopping calculation
# ------------------------------------------------------------

print("\n--- Exercise 17: Shopping ---")

total = 0

price1 = float(input("Enter price of product 1: "))
total += price1

price2 = float(input("Enter price of product 2: "))
total += price2

price3 = float(input("Enter price of product 3: "))
total += price3

print("Total shopping amount:", total)


# ============================================================
# 5. MODULUS OPERATOR
# ============================================================

print("\n--- 5. Modulus Operator ---")

number = int(input("Enter a number: "))

remainder = number % 2

print("Remainder:", remainder)


# ------------------------------------------------------------
# Exercise 18 - Even or odd
# ------------------------------------------------------------

print("\n--- Exercise 18: Even or Odd ---")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is EVEN")
else:
    print("The number is ODD")


# ------------------------------------------------------------
# Exercise 19 - Divisible by 5
# ------------------------------------------------------------

print("\n--- Exercise 19: Divisible by 5 ---")

number = int(input("Enter a number: "))

if number % 5 == 0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")


# ============================================================
# 6. MEMBERSHIP OPERATORS
# ============================================================

print("\n--- 6. Membership Operators ---")

skills = ["Python", "FastAPI", "SQL", "Azure"]

print("Python" in skills)
print("Java" in skills)
print("Java" not in skills)


# ------------------------------------------------------------
# Exercise 20 - Check skill
# ------------------------------------------------------------

print("\n--- Exercise 20: Skill Checker ---")

skills = ["Python", "FastAPI", "SQL", "Azure", "Git"]

skill = input("Enter a skill: ")

if skill in skills:
    print(skill, "is in the skill list")
else:
    print(skill, "is not in the skill list")


# ============================================================
# 7. IDENTITY OPERATORS
# ============================================================

print("\n--- 7. Identity Operators ---")

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a == b:", a == b)
print("a is b:", a is b)

print("a == c:", a == c)
print("a is c:", a is c)


# ============================================================
# 8. OPERATOR PRECEDENCE
# ============================================================

print("\n--- 8. Operator Precedence ---")

result = 10 + 5 * 2

print("10 + 5 * 2 =", result)


result = (10 + 5) * 2

print("(10 + 5) * 2 =", result)


# ------------------------------------------------------------
# Exercise 21 - Calculate total
# ------------------------------------------------------------

print("\n--- Exercise 21: Calculate Total ---")

price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount percentage: "))

subtotal = price * quantity
discount_amount = subtotal * discount / 100
final_price = subtotal - discount_amount

print("Subtotal:", subtotal)
print("Discount:", discount_amount)
print("Final Price:", final_price)


# ============================================================
# 9. PRACTICAL AGE CALCULATOR
# ============================================================

print("\n--- Exercise 22: Age Calculator ---")

birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter current year: "))

age = current_year - birth_year

print("Your approximate age is:", age)


# ============================================================
# 10. SALARY CALCULATOR
# ============================================================

print("\n--- Exercise 23: Salary Calculator ---")

monthly_salary = float(input("Enter monthly salary: "))

annual_salary = monthly_salary * 12

print("Monthly salary:", monthly_salary)
print("Annual salary:", annual_salary)


# ============================================================
# 11. AI ENGINEER PROFILE CALCULATOR
# ============================================================

print("\n--- Exercise 24: AI Engineer Profile ---")

name = input("Enter your name: ")
python_years = float(input("Python experience in years: "))
api_years = float(input("REST API experience in years: "))
sql_years = float(input("SQL experience in years: "))

total_experience = python_years + api_years + sql_years

print("\nAI Engineer Learning Profile")
print("Name:", name)
print("Python:", python_years, "years")
print("REST API:", api_years, "years")
print("SQL:", sql_years, "years")
print("Combined experience:", total_experience, "years")


# ============================================================
# 12. FINAL CHALLENGE
# ============================================================

print("\n" + "=" * 60)
print("FINAL CHALLENGE - AI ENGINEER READINESS CHECK")
print("=" * 60)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
python_years = float(input("Python experience: "))
api_knowledge = input("Do you know REST APIs? (yes/no): ")
sql_knowledge = input("Do you know SQL? (yes/no): ")
git_knowledge = input("Do you know Git? (yes/no): ")

print("\n--- PROFILE ---")

print("Name:", name)
print("Age:", age)
print("Python Experience:", python_years)

print("\n--- SKILL CHECK ---")

print("REST API:", api_knowledge)
print("SQL:", sql_knowledge)
print("Git:", git_knowledge)


# Readiness calculation

python_ready = python_years >= 1
api_ready = api_knowledge == "yes"
sql_ready = sql_knowledge == "yes"
git_ready = git_knowledge == "yes"

ready = python_ready and api_ready and sql_ready and git_ready


print("\n--- RESULT ---")

print("Python ready:", python_ready)
print("REST API ready:", api_ready)
print("SQL ready:", sql_ready)
print("Git ready:", git_ready)

print("AI Engineer Foundation Ready:", ready)


# ============================================================
# END OF PRACTICE FILE
# ============================================================

print("\n" + "=" * 60)
print("TOPIC 04 PRACTICE COMPLETED")
print("=" * 60)