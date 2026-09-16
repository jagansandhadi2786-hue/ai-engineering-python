# ============================================================
# PYTHON FUNDAMENTALS - 23_NUMBER_GUESS
# ============================================================

secret_number = 7

guess = 5

if guess == secret_number:
    print("Correct!")

elif guess < secret_number:
    print("Too low")

else:
    print("Too high")


# Multiple attempts

secret_number = 7
attempts = [3, 5, 8, 7]

for guess in attempts:

    print("Your guess:", guess)

    if guess == secret_number:
        print("Correct!")
        break

    elif guess < secret_number:
        print("Too low")

    else:
        print("Too high")
        
# ============================================================
# END
# ============================================================