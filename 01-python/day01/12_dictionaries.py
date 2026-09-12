# ============================================================
# PYTHON FUNDAMENTALS - TOPIC 5 DICTIONARIES
# ============================================================
#
# Topics:
# 1. Create a dictionary
# 2. Access values
# 3. Add values
# 4. Update values
# 5. Different data types
# 6. Dictionary + list
# 7. Nested dictionaries
# 8. get()
# 9. Check keys
# 10. pop()
# 11. keys(), values(), items()
# 12. JSON-style data
# ============================================================


print("\n" + "=" * 60)
print("TOPIC 5 - PYTHON DICTIONARIES")
print("=" * 60)


# ============================================================
# Exercise 1 - Create a dictionary
# ============================================================

person = {
    "name": "Jagan",
    "age": 30,
    "city": "Hyderabad"
}

print(person)
print(type(person))

# ============================================================
# Exercise 2 - Access values
# ============================================================

print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# ============================================================
# Exercise 3 - Add a new item
# ============================================================

person["country"] = "India"

print(person)

# ============================================================
# Exercise 4 - Update an existing item
# ============================================================

person["city"] = "Bangalore"

print(person)

# ============================================================
# Exercise 5 - Different data types
# ============================================================

employee = {
    "name": "Jagan",
    "age": 30,
    "experience": 14.5,
    "is_active": True
}

print(employee)

print(type(employee["name"]))
print(type(employee["age"]))
print(type(employee["experience"]))
print(type(employee["is_active"]))


# ============================================================
# Exercise 6 - Dictionary containing a list
# ============================================================

employee = {
    "name": "Jagan",
    "skills": [
        "Python",
        "SAP CPI",
        "FastAPI",
        "SQL"
    ]
}

print(employee["name"])
print(employee["skills"])

print("First skill:", employee["skills"][0])
print("Third skill:", employee["skills"][2])


# ============================================================
# Exercise 7 - Nested dictionary
# ============================================================

employee = {
    "name": "Jagan",
    "job": {
        "role": "SAP CPI Developer",
        "experience": 6
    }
}

print(employee["job"]["role"])
print(employee["job"]["experience"])


# ============================================================
# Exercise 8 - get()
# ============================================================

person = {
    "name": "Jagan",
    "age": 30
}

print(person.get("name"))
print(person.get("age"))
print(person.get("salary"))

# ============================================================
# Exercise 9 - Check whether key exists
# ============================================================

print("name" in person)
print("salary" in person)

# ============================================================
# Exercise 10 - Remove using pop()
# ============================================================

person = {
    "name": "Jagan",
    "age": 30,
    "city": "Hyderabad"
}

person.pop("city")

print(person)

# ============================================================
# Exercise 11 - keys()
# ============================================================

person = {
    "name": "Jagan",
    "age": 30,
    "city": "Hyderabad"
}

print(person.keys())

# ============================================================
# Exercise 12 - values()
# ============================================================

print(person.values())

# ============================================================
# Exercise 13 - items()
# ============================================================
print(person.items())
# ============================================================
# Exercise 14 - AI Engineer profile
# ============================================================

ai_profile = {
    "name": "Jagan",
    "current_role": "SAP CPI Developer",
    "target_role": "AI Engineer",
    "python_experience": 1,
    "learning_phase": "Python Fundamentals"
}

print(ai_profile)

print("Current role:", ai_profile["current_role"])
print("Target role:", ai_profile["target_role"])


# ============================================================
# Exercise 15 - Update AI profile
# ============================================================

ai_profile["learning_phase"] = "Python + AI Engineering"

print(ai_profile)


# ============================================================
# Exercise 16 - Add AI skills
# ============================================================

ai_profile["skills"] = [
    "Python",
    "FastAPI",
    "REST API",
    "JSON",
    "SQL"
]

print(ai_profile)


# ============================================================
# Exercise 17 - Access a skill
# ============================================================

print("First AI skill:", ai_profile["skills"][0])
print("Third AI skill:", ai_profile["skills"][2])


# ============================================================
# Exercise 18 - Nested AI configuration
# ============================================================

ai_config = {
    "model": {
        "name": "GPT",
        "temperature": 0.7,
        "max_tokens": 1000
    }
}

print("Model:", ai_config["model"]["name"])
print("Temperature:", ai_config["model"]["temperature"])
print("Max tokens:", ai_config["model"]["max_tokens"])


# ============================================================
# Exercise 19 - JSON-style order data
# ============================================================

order = {
    "orderId": "1001",
    "customerId": "C101",
    "orderType": "B2B",
    "amount": 500,
    "currency": "USD"
}

print("Order ID:", order["orderId"])
print("Customer:", order["customerId"])
print("Order Type:", order["orderType"])
print("Amount:", order["amount"])
print("Currency:", order["currency"])


# ============================================================
# Exercise 20 - Update order
# ============================================================

order["amount"] = 750
order["orderType"] = "B2C"

print(order)


# ============================================================
# Exercise 21 - Add order field
# ============================================================

order["status"] = "Processing"

print(order)
# ============================================================
# Exercise 22 - Safe access with get()
# ============================================================

print(order.get("status"))
print(order.get("paymentMethod"))
print(order.get("deliveryDate"))

# ============================================================
# Exercise 23 - Check keys
# ============================================================

print("orderId" in order)
print("status" in order)
print("paymentMethod" in order)

# ============================================================
# Exercise 24 - Dictionary keys, values and items
# ============================================================

print("Keys:")
print(order.keys())

print("\nValues:")
print(order.values())

print("\nItems:")
print(order.items())

# ============================================================
# Exercise 25 - MINI CHALLENGE
# ============================================================
#
# Create your own AI Engineer profile.
#
# It should contain:
#
# name
# current_role
# target_role
# experience
# skills
# learning_status
#
# Then:
#
# 1. Print the complete dictionary
# 2. Print the target role
# 3. Print the first skill
# 4. Add "Azure"
# 5. Update learning_status
# 6. Print the final dictionary
# ============================================================

my_profile = {
    "name": "Jagan",
    "current_role": "SAP CPI Developer",
    "target_role": "AI Engineer",
    "experience": 6,
    "skills": [
        "Python",
        "FastAPI",
        "REST API"
    ],
    "learning_status": "In Progress"
}

print("\nMy Profile:")
print(my_profile)

print("Target Role:", my_profile["target_role"])

print("First Skill:", my_profile["skills"][0])

my_profile["skills"].append("Azure")

my_profile["learning_status"] = "Python Fundamentals Completed"

print("\nFinal Profile:")
print(my_profile)

print("\n" + "=" * 60)
print("DICTIONARY EXERCISES COMPLETED")
print("=" * 60)