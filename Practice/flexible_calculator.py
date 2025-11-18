#WG 1st Flexible Calculator
#define the sum function
def Sum(*number):
    #get the sum of all items in the list and return it
    result = number.sum()
    return result
    #get the average of all items in the list and return it
def Average(*number):
    length = len(number)
    total = number.sum()
    result = total/length
    return result
    #get the largest number in the list then 
def Max(*number):
    result = number.max()
    return result
    #gets the smallest number and return resul
def Min(*number):
    result = number.min()
    return result
    #gets thr product and returns the result
def Product(*number):
    product = 1
    for m in number:
        product *= m
    result =  product
    return result
#put it all in a while loop to run until they are done
while True:    
    #give user intruduction
    print("Hello, & Welcome to the Flexible Calculator")
    #get the operation that they want to use and display there options
    operation_used = int(input("Do you want \n 1) Sum \n 2) Average \n 3) Max \n 4) Min \n 5) Product \n Please input the number that is assigned to the operation you want to do. \n").strip())
    #ask for the values they want to use in a loop that doesn't end unless input = done
    amount = int(input("How many numbers do you want to input").strip())
    #create empty list numbers
    numbers = []
    for i in range(1,amount+1):
        number= int(input("What is the number"))
        numbers.append(number)
    #if they are finding the sum call sum if they are finding the average call average if they are finding the minimum call min if they are finding the max call max and if they are finding the product call product
    answer = sum(numbers)