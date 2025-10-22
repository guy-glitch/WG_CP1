#WG Ceaser Cipher 1st period
#create list new word
new_word = []
#ask if they want to cipher or decipher
cipher_or_not = int(input("If you want to cipher words press 1 you want to decipher press 2").strip())
# A number assigned to each letter
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# define cipher
def cipher(amount, word):
    #loop through every character in word
    for char in word:
        #checks if char is in the alphabet
        if char in alphabet:
            #find the value of character
            character_value = alphabet.index(char)
            #add the amount of the shift to the value
            new_value = character_value + amount
            #check if new_value is greater then 26
            if new_value > 26:
                # subract 26 from new value to get value
                new_value = new_value - 26
            #convert the value back to a character
            new_letter = alphabet[new_value]
            #add letter to new word list
            new_word.append(new_letter)
        else:
            new_word.append(char)
    #turn list into a stirng join(str(new_word))
    return ''.join(new_word)
# define decipher
def decipher(amount, word):
    #loop through every character in word
    for char in word:
        #checks if char is in the alphabet
        if char in alphabet:
            #find the value of character
            character_value = alphabet.index(char)
            #add the amount of the shift to the value
            new_value = character_value - amount
            #check if new_value is greater then 26
            if new_value < 0:
                # add 26 from new value to get value
                new_value = new_value + 26
            #convert the value back to a character
            new_letter = alphabet[new_value]
            #add letter to new word list
            new_word.append(new_letter)
        else:
            new_word.append(char)
    #turn list into a stirng join(str(new_word))
    return ''.join(new_word)
#if cipher_or_not is cipher
if cipher_or_not == 1:
    # ask how far they want to cipher 
    amount = int(input("Input your cipher amount").strip())
    #ask what word they want to cipher
    word = input("What word do you want to cipher").strip().lower()
    #call cipher in variable result
    result = cipher(amount, word)
    print(f"The Encoded word is {result}")
#else if cipher_or_not is decipher
elif cipher_or_not == 2:
    # ask how far they want to cipher 
    amount = int(input("Input your cipher amount").strip())
    #ask what word they want to cipher
    word = input("What word do you want to cipher").strip().lower()
    #call cipher in variable result
    result = decipher(amount, word)
    print(f"The decoded word is {result}")
else:
    print("Incorrect input run again")