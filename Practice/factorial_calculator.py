#WG 1st factorial Calculator Zane pseudocode
#double hash comments are edits to original pseudocode
#define fact(num)
def fact(num):
    #total = 1, or = num #set total to 1
    total = 1
    #for i in range(0,num)
    for i in range(0, num):
        #total*= num
        total *= num
        #num -= 1
        num -= 1
    #return total
    return total
#while loop
while True:
    #or#switched to num = ask user to give number.strip()#assign it to a variable up here#give instructions please give me a whole non-zero number that you want the factorial of
    num = input("Give me a whole non-zero number that you want the factorial of.").strip()
    #assign that to a vaiable if variable is letters restart
    if num.isdigit():
        #convert variable to float
        num = float(num)
        ##check if variable is a whole non-zero number
        if num.is_integer() and num >= 0:
            ##removed the rounding of num undeeded
            #fact(user_num#just num)
            total = fact(int(num))
            #print(f"new:{total}, original:(or#switched to num)")\
            print(f"Factorial is: {total}, the original number was: {int(num)}")
        else:
            continue
    else:
        continue