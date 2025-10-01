#WG 1st For Loop Notes
listname = [4,15,16,17,287,235,2,654,2542,526364]

for num in listname:
    num/=2
    if num > 100:
        print(f"{num}is only half of {num*2}. It is a large number")
    else:
        print(num)

print("The fruit loop is over")

for num in range(1,10):
    print(num)