# ============================================================
# PYTHON FUNDAMENTALS - 14_WHILE_LOOP
# ============================================================

# 1. Print 1 to 5

number = 1

while number <= 5:
    print(number)
    number += 1

# 2. Countdown

number = 5

while number > 0:
    print(number)
    number -= 1

# 3. Even numbers

number = 2

while number <= 10:
    print(number)
    number += 2

# 4. Sum numbers

number = 1
total = 0

while number <= 10:
    total += number
    number += 1

print("Total:", total)

# 5. Password attempt simulation

attempts = 0

while attempts < 3:
    print("Login attempt:", attempts + 1)
    attempts += 1

print("Maximum attempts reached")