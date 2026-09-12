# ============================================================
# PYTHON FUNDAMENTALS - 13_FOR_LOOP
# ============================================================

# 1. Loop through list

languages = ["Python", "SQL", "Java"]

for language in languages:
    print(language)

# 2. Loop through string

for character in "Python":
    print(character)

# 3. Print numbers

for number in range(1, 6):
    print(number)

# 4. Print even numbers

for number in range(1, 11):
    if number % 2 == 0:
        print(number)

# 5. Calculate total

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total += number

print("Total:", total)

# 6. Find largest number

numbers = [10, 50, 30, 90, 20]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest:", largest)

# 7. AI skills

skills = ["Python", "FastAPI", "REST API", "Docker"]

for skill in skills:
    print("Learning:", skill)