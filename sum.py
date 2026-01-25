# ask the user for 5 numbers 
# add them up
# print the total
total=0
for i in range (5):
    num=int(input("Enter 5 numbers"))
    total +=num
    print(total)
#while loop version
total=0
counter=1
while counter<=5:
    num=int(input("enter any 5 numbers"))
    total+=num
    count+=1
    print (total)
    # rule of thumb
    # 1 start with 0 in the total before the loop
    # 2 inside the loop total+=numbers
    # 3 print out the total after the loop

# times table of a number
mult=0
for i in range(12):
    num=int(input("input a number: "))
    mult*=num
    print (mult)
    
    
