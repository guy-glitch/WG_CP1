#WG 1st password strength checker
#ask for the users password
password = input("What is your password that you want to check the strength of?").strip()
#get length of password
password_len = len(password)
#list of special characters
special = "(!@#$%^&*()_+-=[]{}|;:,.<>?)"
#score = 0
score = 0
#for characters in password
for char in password:
    #if length is upper
    if char.isupper():
            #score + 1
        score += 1
            #break out of loop
        break
#for length of password
for char in password:
    #if length is lower
    if char.islower(): 
            #score + 1
        score += 1
            #break out of loop
        break
#for length of password
for char in password:
    #if length is num
    if char.isdigit():
            #score + 1
        score += 1
            #break out of loop
        break
#for length of password
for char in password:
    #if length in special
    if char in special:
            #score + 1
        score += 1
            #break out of loop
        break
#if length >= 8
if  password_len >= 8:
    #score + 1
    score += 1
#else
else:
    #display  
    print("      ") 
#check if score is 5 set strength to very strong
if score == 5:
     strength = "Very strong"
#or check if score is 4 set strength to strong
elif score == 4:
     strength = "Strong"
#or check if score is 3 set strength to moderate
elif score == 3:
     strength = "Moderate"
#else
else:
     strength = "Weak"
# display score/5 and password strength
print(f"Strength score : {score}/5 \nPassword strength: {strength}")