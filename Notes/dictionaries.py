#WG dictionaries notes 1st

#key: Value pairs

person = {
    #key:value,
    "name": "Xavier",
    "age": 22,
    "job": "Mavrick",
    "sibling":["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Jake"]
}
print(f"Name is {person["name"]}")
print(person.keys())
for key in person.keys():
    print(f"{key} is {person[key]}")