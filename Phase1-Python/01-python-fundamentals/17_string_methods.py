# ============================================================
# PYTHON FUNDAMENTALS - 17_STRING_METHODS
# ============================================================

text = "Python AI Engineering"

# upper
print(text.upper())

# lower
print(text.lower())

# capitalize
print(text.capitalize())

# title
print(text.title())

# strip
name = "   Jagan   "
print(name.strip())

# replace
print(text.replace("Python", "Advanced Python"))

# split
skills = "Python,SQL,FastAPI,Docker"
skill_list = skills.split(",")

print(skill_list)

# join
result = " | ".join(skill_list)
print(result)

# startswith
print(text.startswith("Python"))

# endswith
print(text.endswith("Engineering"))

# find
print(text.find("AI"))

# count
print(text.count("n"))

# Practice

email = "jagan@example.com"

print(email.lower())
print(email.strip())
print(email.endswith(".com"))
print("@" in email)

# ============================================================
# END
# ============================================================