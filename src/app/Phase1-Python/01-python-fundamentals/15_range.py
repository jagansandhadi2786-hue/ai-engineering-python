# ============================================================
# PYTHON FUNDAMENTALS - 15_RANGE
# ============================================================

# 1. range(stop)

for number in range(5):
    print(number)

# 2. range(start, stop)

for number in range(1, 6):
    print(number)

# 3. range(start, stop, step)

for number in range(2, 11, 2):
    print(number)

# 4. Countdown

for number in range(10, 0, -1):
    print(number)

# 5. Odd numbers

for number in range(1, 20, 2):
    print(number)

# 6. Multiplication table

number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# 7. Sum

total = 0

for number in range(1, 101):
    total += number

print("Sum:", total)

# ============================================================
# END
# ============================================================