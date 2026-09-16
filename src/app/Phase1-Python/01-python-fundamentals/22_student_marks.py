# ============================================================
# PYTHON FUNDAMENTALS - 22_STUDENT_MARKS
# ============================================================

def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):

    if average >= 90:
        return "A"

    elif average >= 75:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"


# Student data

student_name = "Rahul"

marks = [85, 78, 92, 88, 76]

total = calculate_total(marks)
average = calculate_average(marks)
grade = calculate_grade(average)

print("Student:", student_name)
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)

# Pass/fail

if average >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")
    
# ============================================================
# END
# ============================================================