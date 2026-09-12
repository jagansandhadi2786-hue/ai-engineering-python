# ============================================================
# PYTHON FUNDAMENTALS - 11_SETS
# ============================================================

# 1. Create set

languages = {"Python", "Java", "SQL"}
print(languages)

# 2. Duplicate removal

numbers = {1, 2, 2, 3, 3, 4}
print(numbers)

# 3. Add item

languages.add("Docker")
print(languages)

# 4. Remove item

languages.remove("Java")
print(languages)

# 5. Discard item

languages.discard("C++")
print(languages)

# 6. Membership

print("Python" in languages)

# 7. Set union

a = {"Python", "SQL"}
b = {"Python", "Docker"}

print(a | b)

# 8. Set intersection

print(a & b)

# 9. Set difference

print(a - b)

# 10. Convert list to set

items = ["Python", "Python", "SQL", "SQL"]
unique_items = set(items)

print(unique_items)