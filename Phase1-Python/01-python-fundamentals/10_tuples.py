# ============================================================
# PYTHON FUNDAMENTALS - 10_TUPLES
# ============================================================

# 1. Create tuple

languages = ("Python", "Java", "SQL")
print(languages)

# 2. Access items

print(languages[0])
print(languages[-1])

# 3. Tuple length

print(len(languages))

# 4. Tuple slicing

numbers = (10, 20, 30, 40, 50)

print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

# 5. Tuple unpacking

name, age, role = ("Jagan", 30, "AI Engineer")

print(name)
print(age)
print(role)

# 6. Single item tuple

item = ("Python",)
print(item)

# 7. Tuple methods

values = (10, 20, 20, 30)

print(values.count(20))
print(values.index(30))

# 8. List vs tuple

my_list = ["Python", "SQL"]
my_tuple = ("Python", "SQL")

print(my_list)
print(my_tuple)