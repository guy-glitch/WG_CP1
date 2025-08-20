#WG, Hello World project
#Prints login page
print("Please Login")
#Greets users by name and if they are returning user
returning = ("Dirk, Miari, Bryor, Brecken, Milo")
admin = ("Warren, Ms. LaRose")
# asks for name and if it is an admin does not auto capitilize other wise it capitilzes
name = input("what is your name")
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

