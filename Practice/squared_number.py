#WG Squared Numbers 1st 
#list of numbers
original_num=[3,7,12,25,30,45,50,65,70,85,90,105,110,125,130,145,150,165,170,185,190,205,210,225,230,245,250,265,270,285]
#set squared num to lambda num:num**
squared=list(map(lambda num:num*num, original_num))
#loop through squared_num for nice printing,  #display Original: original num, squared: num
for num in squared:print(f"Original: {original_num[squared.index(num)]}, Squared: {num}")