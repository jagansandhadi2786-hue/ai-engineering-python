# ============================================================
# PYTHON FUNDAMENTALS - 19_BOOLEAN_LOGIC
# ============================================================

# AND

age = 25
has_id = True

print(age >= 18 and has_id)

# OR

is_admin = False
is_manager = True

print(is_admin or is_manager)

# NOT

logged_in = False

print(not logged_in)

# Practical login

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")

# AI Engineer eligibility

python_score = 80
sql_score = 75
has_project = True

if python_score >= 60 and sql_score >= 60 and has_project:
    print("Eligible")

# API access

role = "developer"
active = True

if (role == "admin" or role == "developer") and active:
    print("API access granted")
else:
    print("Access denied")
    
# ============================================================
# END
# ============================================================