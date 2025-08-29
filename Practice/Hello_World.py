#WG, Hello World project
#Prints login page
print("Please Login")
#Greets users by name and if they are returning user
admin = ("Warren, Ms. LaRose")
returning = ("Dirk, Miari, Bryor, Brecken, Milo")
name = input("What is your name")
user = (f"{admin}, {returning} + {name}")
password_new = input("enter your password")
password_larose = ("programming")
password_warren = ("skills")
if name == "Ms. LaRose":
    if password_new == password_larose:
        name = name 
        print(f"Hello Admin {name}")
if name == "Warren":
    if password_new == password_warren:
        name = name.capitalize()
        print(f"Hello World")
# asks for name and if it is an admin does not auto capitilize other wise it capitilzes
if name == "Ms. LaRose":
    name = name
else:
    name = name.capitalize()
if name in admin:
    print(f"Hello Admin {name}")
elif name in returning:
    print(f"Welcome back {name}")
else:
    print(f"Hello {name}")

