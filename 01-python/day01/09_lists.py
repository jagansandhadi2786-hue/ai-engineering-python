# ============================================================
# PYTHON FUNDAMENTALS - 09_LISTS
# ============================================================

# 1. Create list

languages = ["Python", "Java", "JavaScript"]
print(languages)

# 2. Access items

print(languages[0])
print(languages[1])
print(languages[-1])

# 3. Change item

languages[1] = "C++"
print(languages)

# 4. Add item

languages.append("SQL")
print(languages)

# 5. Insert item

languages.insert(1, "Python")
print(languages)

# 6. Remove item

languages.remove("C++")
print(languages)

# 7. Pop item

removed = languages.pop()
print("Removed:", removed)
print(languages)

# 8. List length

print(len(languages))

# 9. List slicing

numbers = [10, 20, 30, 40, 50]

print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

# 10. Practice

ai_tools = ["Python", "FastAPI", "LangChain"]

ai_tools.append("Docker")
ai_tools.append("Azure")

print(ai_tools)