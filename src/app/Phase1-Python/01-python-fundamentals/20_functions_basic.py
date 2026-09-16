# ============================================================
# PYTHON FUNDAMENTALS - 20_FUNCTIONS_BASIC
# ============================================================

# 1. Basic function

def greet():
    print("Hello Python")


greet()

# 2. Function with parameter

def greet_user(name):
    print("Hello", name)


greet_user("Jagan")

# 3. Multiple parameters

def add(a, b):
    print(a + b)


add(10, 20)

# 4. Return value

def multiply(a, b):
    return a * b


result = multiply(5, 4)

print(result)

# 5. Default parameter

def welcome(name="User"):
    print("Welcome", name)


welcome()
welcome("Jagan")

# 6. Calculate square

def square(number):
    return number * number


print(square(5))

# 7. Check even

def is_even(number):
    return number % 2 == 0


print(is_even(10))
print(is_even(7))

# 8. AI-style function

def create_model_config(model, temperature):
    return {
        "model": model,
        "temperature": temperature
    }


config = create_model_config("gpt-model", 0.7)

print(config)

# ============================================================
# END
# ============================================================