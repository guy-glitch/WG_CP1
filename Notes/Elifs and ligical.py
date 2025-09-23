#WG_1st_elif and logical operators notes
grade = float(input("What is your percentage grade").strip())

if grade > 100:
    print(f"You did extra credit. . . you did {grade - 100}% extra credit")
elif grade == 100:
    print("Your grade is perfect")
elif grade >= 92:
    print(f"You have an A at {grade}%")
elif grade >= 80 and grade <= 90:
    print(f"You have a B in the class at {grade}%")
else:
    print("You are a failure, get better.")