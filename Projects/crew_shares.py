#WG_1st_Crew_Shares
print("You are a pirate captain, tell me how many crew members there are and how much money you made.")

crew_member = int(input("How many crew members are there?"))

money_made = float(input("How much money did you make?"))

shares = float(money_made/(crew_member+10))

crew_shares = float(shares-500)

print(f"Here is the amount that still needs to be payed to each crew member ${crew_shares:.2f}")

print(f"Here is how much the first mate gets paid ${(shares*3):.2f}")

print(f"The captain gets ${(shares*7):.2f}")





