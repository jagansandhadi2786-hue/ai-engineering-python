# ============================================================
# PYTHON FUNDAMENTALS - 05_STRINGS
# ============================================================

# 1. Create a string
name = "Jagan"
print(name)

# 2. String length
print(len(name))

# 3. Access characters
print(name[0])
print(name[-1])

# 4. String slicing
message = "AI Engineer"
print(message[0:2])
print(message[:2])
print(message[3:])
print(message[::-1])

# 5. Concatenation
first_name = "Jagan"
last_name = "Reddy"
full_name = first_name + " " + last_name
print(full_name)

# 6. Repeat string
print("AI " * 3)

# 7. Check substring
text = "Python is important for AI"
print("Python" in text)
print("Java" in text)

# 8. Multiline string
description = """
Python is used for:
- AI
- Automation
- APIs
"""
print(description)

# 9. String formatting
age = 30
print(f"My name is {name} and I am {age} years old.")

# 10. Practice
course = "Python for AI Engineering"
print("Course:", course)
print("Length:", len(course))
print("First character:", course[0])
print("Last character:", course[-1])