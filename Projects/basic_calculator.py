#WG_1st_Calculator
running = True

while running:
    run =input("would you like to run again?").lower().strip()
    if run == "no":
        running = False
    else:
       first_number = int(input("What is the first number in the equation?").strip())
       second_number = int(input("What is the second number in the equation?").strip())
       addition = (first_number + second_number)
       division = (first_number/second_number )
       subtraction = (first_number-second_number)
       multiplication = (first_number*second_number)
       exponents = (first_number**second_number)
       modulo = (first_number%second_number)
       integer_division = (first_number//second_number)
       #prints the answers to the equations
       print(f"{first_number} + {second_number} = {addition}")
        print(f"{first_number} - {second_number} = {subtraction}")
        print(f"{first_number} * {second_number} = {multiplication}")
        print(f"{first_number} / {second_number} = {division}")
        print(f"{first_number} ** {second_number} = {exponents}")
        print(f"{first_number} % {second_number} = {modulo}")
        print(f"{first_number} // {second_number} = {integer_division}")

