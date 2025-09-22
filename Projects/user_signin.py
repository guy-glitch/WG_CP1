#WG_1st_User_Sign_In
number_of_logins = 4
while number_of_logins > 0:
    username = input("What is your username? ").strip().lower()
    if username == "warren.gibson@ucas-edu.net":
        while number_of_logins > 0:
            password = input("Enter your password! ").strip().lower()
            if password == "1443":
                print("Welcome, Warren")
                number_of_logins = 0
            else:
                number_of_logins -= 1
                print(f"Incorrect password. You have {number_of_logins} login attempts left.")
    else:
        number_of_logins -= 1
        print(f"Incorrect user name. You have {number_of_logins} logins attempts left.")