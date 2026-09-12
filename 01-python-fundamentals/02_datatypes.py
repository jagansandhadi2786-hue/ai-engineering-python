# ==========================================
# 02 - Python Data Types
# ==========================================

# 1. STRING-A str stores text.
name = "Jagan"
role = "AI Engineer"
model_name = "GPT"

print("Name:", name)
print("Role:", role)
print("model_name:", model_name)
print("Type:", type(name))


# 2. INTEGER-An int stores whole numbers.
age = 30
experience = 14
max_tokens = 1000
user_count = 250

print("Age:", age)
print("Experience:", experience)
print("Max Tokens:", max_tokens)
print("user_count:", user_count)
print("Type:", type(age))


# 3. FLOAT-A float stores numbers containing decimals.
price = 100.50
temperature = 0.7
confidence_score = 0.92
api_cost = 0.0025

print("Price:", price)
print("Temperature:", temperature)
print("Confidence:", confidence_score)
print("api_cost:", api_cost)
print("Type:", type(price))


# 4. BOOLEAN-A Boolean has only two possible values:T or F
is_active = True
is_admin = False
api_enabled = True

print("Active:", is_active)
print("Admin:", is_admin)
print("api_enabled:", api_enabled)
print("Type:", type(is_active))


# 5. LIST-Collection of items, A list stores multiple values.
models = ["GPT", "Claude", "Gemini"]

print("Models:", models)
print("First model:", models[0])
print("Type:", type(models))


# 6. TUPLE-Fixed Collection-A tuple looks similar to a list, but uses:()
response_formats = ("JSON", "XML", "TEXT")

print("Response formats:", response_formats)
print("Type:", type(response_formats))


# 7. SET-A set stores unique values.
skills = {"Python", "AI", "Python", "FastAPI"}

print("Skills:", skills)
print("Type:", type(skills))

# 8. DICTIONARY-Dictionary - This is one of the most important Python data types for AI engineering. A dictionary stores:key → value
# because JSON looks almost exactly like Python dictionaries.

user = {
    "name": "Jagan",
    "age": 30,
    "role": "AI Engineer"
}

print("User:", user)
print("User name:", user["name"])
print("Type:", type(user))


# 9. NONE-No Value
error_message = None

print("Error:", error_message)
print("Type:", type(error_message))

# ------------------------------------------------------------

print("=" * 60)
print("PYTHON LISTS - HANDS-ON EXERCISES")
print("=" * 60)

# ------------------------------------------------------------
# Exercise 1 -  Create and identify str, int, float, bool
# ------------------------------------------------------------
print("\nExercise 1 - Create and identify str, int, float, bool")
name = "Jagan"
age = 30
experience = 14
salary = 15.5
is_learning_python = True

print(name, type(name))
print(age, type(age))
print(experience, type(experience))
print(salary, type(salary))
print(is_learning_python, type(is_learning_python))

# Create and access a list using indexes
# Python Day 1 - Exercise 2: Lists and Indexes
# Topic: Create and access a list using indexes

# ------------------------------------------------------------
# Exercise 1 - Create a list
# ------------------------------------------------------------
print("\nExercise 1 - Create a list")
skills = ["Python", "SAP CPI", "FastAPI", "SQL", "Azure"]
print(skills)
# ------------------------------------------------------------
# Exercise 2 - Access the first item
# ------------------------------------------------------------
print("\nExercise 2 - Access the first item")
print(skills[0])
# ------------------------------------------------------------
# Exercise 3 - Access the third item
# ------------------------------------------------------------
print("\nExercise 3 - Access the third item")
print(skills[2])
# ------------------------------------------------------------
# Exercise 4 - Access the last item using negative index
# ------------------------------------------------------------
print("\nExercise 4 - Access the last item")
print(skills[-1])
# ------------------------------------------------------------
# Exercise 5 - Find the length of the list
# ------------------------------------------------------------
print("\nExercise 5 - Find the number of items")
print(len(skills))
# ------------------------------------------------------------
# Exercise 6 - Mixed data types
# ------------------------------------------------------------
print("\nExercise 6 - Mixed data types")
person = ["Jagan", 30, 14, 15.5, True]
print(person)

print(type(person[0]))
print(type(person[1]))
print(type(person[2]))
print(type(person[3]))
print(type(person[4]))
# ------------------------------------------------------------
# Exercise 7 - Predict the output
# ------------------------------------------------------------
print("\nExercise 7 - Predict the output before running")
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
print(numbers[-1])
print(numbers[-3])
# ------------------------------------------------------------
# Exercise 8 - Your own AI Engineering skills list
# ------------------------------------------------------------
print("\nExercise 8 - Create your own AI Engineering skills list")

ai_skills = [
    "Python",
    "FastAPI",
    "LLMs",
    "RAG",
    "LangChain"
]

print("First skill:", ai_skills[0])
print("Third skill:", ai_skills[2])
print("Last skill:", ai_skills[-1])
print("Number of skills:", len(ai_skills))
# ------------------------------------------------------------
# Bonus Exercise - Index practice
# ------------------------------------------------------------
print("\nBonus Exercise - Index practice")

technologies = ["Python", "FastAPI", "REST API", "JSON", "SQL", "Azure"]

print("First:", technologies[0])
print("Second:", technologies[1])
print("Fourth:", technologies[3])
print("Last:", technologies[-1])
print("Second last:", technologies[-2])
print("Total:", len(technologies))


print("\n" + "=" * 60)
print("END OF EXERCISES")
print("=" * 60)


# Add/remove items from a list
skills = ["Python", "FastAPI", "SQL"]

# Add at the end
skills.append("Azure")

# Add at index 1
skills.insert(1, "REST API")

# Remove a value
skills.remove("SQL")

# Remove item at index 0
skills.pop(0)

print(skills)


# ============================================================
# PYTHON FUNDAMENTALS - COMBINED HANDS-ON EXERCISES
# Topics 1-4
# ============================================================
#
# Topic 1: str, int, float, bool
# Topic 2: Lists and indexes
# Topic 3: append, insert, remove, pop
# Topic 4: List slicing
# ============================================================


# ============================================================
# TOPIC 1 - DATA TYPES
# ============================================================

print("\n" + "=" * 60)
print("TOPIC 1 - DATA TYPES")
print("=" * 60)


# Exercise 1 - Create and identify data types

name = "Jagan"
age = 30
experience = 14.5
is_learning_python = True

print(name, type(name))
print(age, type(age))
print(experience, type(experience))
print(is_learning_python, type(is_learning_python))


# Exercise 2 - Identify city

city = "Hyderabad"

print("City:", city)
print("Type:", type(city))


# Exercise 3 - Identify years

years = 14

print("Years:", years)
print("Type:", type(years))


# Exercise 4 - Identify percentage

percentage = 85.5

print("Percentage:", percentage)
print("Type:", type(percentage))


# Exercise 5 - Identify boolean

is_employee = True

print("Is employee:", is_employee)
print("Type:", type(is_employee))


# ============================================================
# TOPIC 2 - LISTS AND INDEXES
# ============================================================

print("\n" + "=" * 60)
print("TOPIC 2 - LISTS AND INDEXES")
print("=" * 60)


# Exercise 6 - Create a list

skills = ["Python", "SAP CPI", "FastAPI", "SQL", "Azure"]

print(skills)
print(type(skills))


# Exercise 7 - Access first item

print("First item:", skills[0])


# Exercise 8 - Access third item

print("Third item:", skills[2])


# Exercise 9 - Access last item

print("Last item:", skills[-1])


# Exercise 10 - Find list length

print("Number of skills:", len(skills))


# Exercise 11 - Mixed data types

person = ["Jagan", 30, 14.5, True]

print(person)

print(type(person[0]))
print(type(person[1]))
print(type(person[2]))
print(type(person[3]))


# Exercise 12 - Predict the output

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
print(numbers[-1])
print(numbers[-3])


# Exercise 13 - AI Engineering skills

ai_skills = [
    "Python",
    "FastAPI",
    "LLMs",
    "RAG",
    "LangChain"
]

print("First:", ai_skills[0])
print("Third:", ai_skills[2])
print("Last:", ai_skills[-1])
print("Total:", len(ai_skills))


# ============================================================
# TOPIC 3 - ADD, CHANGE AND REMOVE ITEMS
# ============================================================

print("\n" + "=" * 60)
print("TOPIC 3 - ADD, CHANGE AND REMOVE ITEMS")
print("=" * 60)


# Exercise 14 - append()

languages = ["Python", "Java", "JavaScript"]

languages.append("C#")

print(languages)


# Exercise 15 - insert()

skills = ["Python", "SQL", "Azure"]

skills.insert(1, "FastAPI")

print(skills)


# Exercise 16 - remove()

skills = ["Python", "FastAPI", "SQL", "Java"]

skills.remove("Java")

print(skills)


# Exercise 17 - pop() using index

skills = ["Python", "FastAPI", "SQL", "Azure"]

skills.pop(2)

print(skills)


# Exercise 18 - pop() without index

skills = ["Python", "FastAPI", "SQL", "Azure"]

skills.pop()

print(skills)


# Exercise 19 - Combine append, insert, remove, pop

ai_skills = ["Python", "SQL"]

ai_skills.append("FastAPI")
ai_skills.insert(1, "REST API")
ai_skills.remove("SQL")
ai_skills.pop()

print(ai_skills)


# Exercise 20 - AI Engineering skills

ai_skills = [
    "Python",
    "FastAPI",
    "REST API",
    "JSON",
    "SQL"
]

ai_skills.append("Pydantic")
ai_skills.insert(1, "Git")
ai_skills.remove("JSON")
ai_skills.pop()

print(ai_skills)
print("Number of skills:", len(ai_skills))


# ============================================================
# TOPIC 4 - LIST SLICING
# ============================================================

print("\n" + "=" * 60)
print("TOPIC 4 - LIST SLICING")
print("=" * 60)


# Exercise 21 - Basic slicing

skills = ["Python", "FastAPI", "SQL", "Azure", "LLMs"]

print(skills[1:4])

# Exercise 22 - Start from beginning

print(skills[:3])

# Exercise 23 - Start from index 2

print(skills[2:])

# Exercise 24 - Copy the whole list

print(skills[:])

# Exercise 25 - Last three items

print(skills[-3:])

# Exercise 26 - First two items

print(skills[:2])

# Exercise 27 - Items from index 1 to index 3

print(skills[1:3])

# Exercise 28 - Every second item

numbers = [1, 2, 3, 4, 5, 6]
print(numbers[::2])

# Exercise 29 - Every second item starting from index 1
print(numbers[1::2])
# Exercise 30 - Reverse the list
print(skills[::-1])
# Exercise 31 - Reverse numbers
print(numbers[::-1])
# Exercise 32 - Negative slicing
print(skills[-4:-1])
# Exercise 33 - Slice with start, end and step
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[1:7:2])

# ============================================================
# TOPIC 4 - AI ENGINEERING MINI CHALLENGE
# ============================================================

print("\n" + "=" * 60)
print("AI ENGINEERING MINI CHALLENGE")
print("=" * 60)


technologies = [
    "Python",
    "FastAPI",
    "REST API",
    "JSON",
    "SQL",
    "Git",
    "Azure",
    "LLMs",
    "RAG",
    "LangChain"
]

# 1. Print first three technologies
print("First three:", technologies[:3])

# 2. Print last three technologies
print("Last three:", technologies[-3:])

# 3. Print technologies from index 2 to 5
print("Index 2 to 5:", technologies[2:6])

# 4. Print every second technology
print("Every second:", technologies[::2])

# 5. Print the list in reverse
print("Reverse:", technologies[::-1])

# 6. Print total number of technologies
print("Total:", len(technologies))


# ============================================================
# END
# ============================================================

print("\n" + "=" * 60)
print("ALL EXERCISES COMPLETED")
print("=" * 60)

# Create a tuple

# Explain list vs tuple

# Create a set and understand duplicate removal


# Read, update, and add dictionary values

# Explain why dictionaries are important for JSON/API work



# Understand None
# Use type() confidently
# Complete the AI Model Configuration mini-project