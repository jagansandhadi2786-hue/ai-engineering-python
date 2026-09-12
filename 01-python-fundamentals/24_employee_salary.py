# ============================================================
# PYTHON FUNDAMENTALS - 24_EMPLOYEE_SALARY
# ============================================================

def calculate_bonus(salary, performance):

    if performance == "excellent":
        return salary * 0.20

    elif performance == "good":
        return salary * 0.10

    elif performance == "average":
        return salary * 0.05

    else:
        return 0


def calculate_total_salary(salary, bonus):
    return salary + bonus


# Employee details

employee_name = "Jagan"
salary = 100000
performance = "excellent"

bonus = calculate_bonus(salary, performance)

total_salary = calculate_total_salary(
    salary,
    bonus
)

print("Employee:", employee_name)
print("Basic Salary:", salary)
print("Performance:", performance)
print("Bonus:", bonus)
print("Total Salary:", total_salary)

# Salary category

if total_salary >= 120000:
    print("Salary Category: High")

elif total_salary >= 100000:
    print("Salary Category: Medium")

else:
    print("Salary Category: Standard")