#WG_1st_String_Methods
#subject = "computer programing 1"

#print(subject.capitalize())

#print(subject.center(100))

#Stupid/Idiot Proffing Inputs
#color = input("What is your favorite color?").strip().upper().swapcase()
#print(f"That is cool. I like {color}, to")

#name = input("What is your name").strip().title()
#print(name)


#print(f"That is a cool color I like {color} to {name}")
#pi = "3.1415926"
#print
#print(pi.isdecimal())
sentence = ("The quick brown fox jumps over the lazy dog.")
word = "jumps"
print(sentence.find(word))
start = sentence.index(word)
length = len(word)
print(sentence[start:start+length])
print(sentence.replace(word, "swims"))



