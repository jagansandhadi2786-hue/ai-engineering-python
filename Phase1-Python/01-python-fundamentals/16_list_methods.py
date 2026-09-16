# ============================================================
# PYTHON FUNDAMENTALS - 16_LIST_METHODS
# ============================================================

numbers = [10, 20, 30, 20, 40]

# append
numbers.append(50)
print(numbers)

# insert
numbers.insert(1, 15)
print(numbers)

# remove
numbers.remove(20)
print(numbers)

# pop
removed = numbers.pop()
print("Removed:", removed)

# count
print("20 count:", numbers.count(20))

# index
print("Index:", numbers.index(30))

# sort
numbers.sort()
print(numbers)

# reverse
numbers.reverse()
print(numbers)

# copy
new_numbers = numbers.copy()
print(new_numbers)

# clear
new_numbers.clear()
print(new_numbers)

# Practical example

skills = ["Python", "SQL", "FastAPI"]

skills.append("Docker")
skills.insert(1, "REST API")
skills.remove("SQL")

print(skills)

# ============================================================
# END
# ============================================================