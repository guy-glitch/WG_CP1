#WG 1st Letter Grade
grade = float(input("What is your percentage grade, to the decimal point").strip())
if grade > 92:
    print(f"You have an A, at {grade}%, great job")
elif grade > 90 and grade < 92:
    print(f"You have an A-, at {grade}%, good job")
elif grade > 87 and grade < 90:
    print(f"You have an B+, at {grade}%, good job")
elif grade >= 82 and grade < 87:
    print(f"You have an B, at {grade}%, good job you could improve")
elif grade >= 80 and grade < 82:
    print(f"You have an B-, at {grade}%, You should work a little bit on that")
elif grade > 77 and grade < 80:
    print(f"You have an C+, at {grade}%, You need to work on that a little")
elif grade > 72 and grade < 77:
    print(f"You have an C, at {grade}%, depressing you should get better")
elif grade > 70 and grade < 72:
    print(f"You have an C-, at {grade}%, have a slightly better life and maybe you will pass")
elif grade > 67 and grade < 70:
    print(f"You have an D+, at {grade}%, Fix this or get debt.")
elif grade > 64 and grade < 67:
    print(f"You have an D, at {grade}%, you need to get help to fix this")
elif grade > 55 and grade < 64:
    print(f"You have an D-, at {grade}%, stop being a failure and get some help")
elif grade < 55:
    print(f"You have an F, at {grade}%, stop being a failure and get some help. You must have scored low on the gene pool")
else:
    print(f"Incorrect input get better, you must have scored really low on the gene pool")