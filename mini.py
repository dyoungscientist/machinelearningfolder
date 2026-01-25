# mini challenge
# ask user for numbers until they type in 0
# add the total numbeers inputed

stop=0
usernum=1
total=0
while usernum!=stop:
    usernum=int(input("enter a number pleaseee"))
    total+=usernum
    if usernum!=stop:
        print (total)