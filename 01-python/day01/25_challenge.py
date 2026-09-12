# ============================================================
# PYTHON FUNDAMENTALS - 25_CHALLENGE
# ============================================================
# MINI PROJECT: AI ENGINEER PROFILE SYSTEM
# ============================================================

# ------------------------------------------------------------
# 1. Employee / Student information
# ------------------------------------------------------------

name = "Jagan"
age = 30
role = "SAP CPI Developer"
target_role = "AI Engineer"

skills = [
    "Python",
    "REST API",
    "FastAPI",
    "SQL",
    "Docker"
]

print("======================================")
print("       AI ENGINEER PROFILE")
print("======================================")

print("Name:", name)
print("Age:", age)
print("Current Role:", role)
print("Target Role:", target_role)

# ------------------------------------------------------------
# 2. Display skills
# ------------------------------------------------------------

print("\nSkills:")

for skill in skills:
    print("-", skill)

# ------------------------------------------------------------
# 3. Python readiness
# ------------------------------------------------------------

python_score = 75
sql_score = 65
api_score = 70

print("\nLearning Scores")

print("Python:", python_score)
print("SQL:", sql_score)
print("REST API:", api_score)

# ------------------------------------------------------------
# 4. Calculate average
# ------------------------------------------------------------

average = (
    python_score +
    sql_score +
    api_score
) / 3

print("Average:", average)

# ------------------------------------------------------------
# 5. Determine readiness
# ------------------------------------------------------------

if average >= 80:

    print("Status: Excellent")

elif average >= 60:

    print("Status: Ready for next phase")

else:

    print("Status: Need more practice")

# ------------------------------------------------------------
# 6. Check individual skills
# ------------------------------------------------------------

if "Python" in skills:
    print("Python skill available")

if "REST API" in skills:
    print("REST API skill available")

if "FastAPI" in skills:
    print("FastAPI skill available")

# ------------------------------------------------------------
# 7. Function
# ------------------------------------------------------------

def calculate_readiness(score):

    if score >= 80:
        return "Advanced"

    elif score >= 60:
        return "Intermediate"

    else:
        return "Beginner"


print("\nSkill Level:")
print("Python:", calculate_readiness(python_score))
print("SQL:", calculate_readiness(sql_score))
print("API:", calculate_readiness(api_score))

# ------------------------------------------------------------
# 8. Create profile dictionary
# ------------------------------------------------------------

profile = {
    "name": name,
    "age": age,
    "current_role": role,
    "target_role": target_role,
    "skills": skills,
    "average_score": average
}

print("\nProfile:")
print(profile)

# ------------------------------------------------------------
# 9. Final decision
# ------------------------------------------------------------

if (
    python_score >= 60
    and sql_score >= 60
    and api_score >= 60
):

    print("\nFinal Result:")
    print("Ready to continue AI Engineering learning path.")

else:

    print("\nFinal Result:")
    print("Continue Python/API practice.")