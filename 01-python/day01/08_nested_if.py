# ============================================================
# PYTHON FUNDAMENTALS - 08_NESTED_IF
# ============================================================

# 1. Nested age and ID check

age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")

# 2. Login with role

username = "admin"
password = "1234"
role = "developer"

if username == "admin":
    if password == "1234":
        if role == "developer":
            print("Developer access granted")
        else:
            print("Different role")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# 3. Student result

marks = 85
attendance = 90

if marks >= 50:
    if attendance >= 75:
        print("Student passed")
    else:
        print("Attendance too low")
else:
    print("Marks too low")

# 4. AI Engineer eligibility

python_score = 80
sql_score = 70

if python_score >= 60:
    if sql_score >= 60:
        print("Eligible for AI Engineering training")
    else:
        print("Improve SQL")
else:
    print("Improve Python")