# okay... so... yeah... learning python...
"""
so baiscally this is a test file for learning basics of python
i will be adding code snippets here to learn python
and practicing it
Resources:
1. W3Schools
2. GeeksforGeeks
3. PythonWorkbook by Jaime chan 
topics : variables, loops, functions
write short notes 
"""
 # date : 03-09-25 chapter 3 of python workbook
 # the world of variables and operators
# variables are used to store data
# operators are used to perform operations on variables
"""
myFavNumber = 11
myFavString = 'Python'
userName = 'Lee'
print (userName)
userName = 'James'
print (userName)
x, y = 5, 4
print (x//y)
print (x%y)
print (x**y)
a, b = 12, 5
print (a*b)
remainder = a//b
print (remainder)
print (a + b)
a, b, c = 13, 7, 5
result = (a+c)*b+c-a
print (result)
"""
# date : 04-09-25
# topic: loops: if/else/else if 
"""
equals: a==b
not equals: a!=b
greater-than:a>b
greater-than or equal to: a>=b
less than:a<b
less than or equal to: a<=b
"""
a =33
b =22 
if a<b:
    print("a is less than b!") #there must be whitespace
else:
    print("a is greater than b!")

x=9
y=10
if x<y:
   print("x is less  than y")
elif x==y:
    print("x is equal to y")

    g=21
    h=81
    if g<h:
        print("g is less than h !")
    elif g == h:
        print(" g is is h")
    else: 
        print("g is not h")
#shorthand syntax
w=00
r=50
if w<r: print("w is less than r")

t=90
u=00 
print ("T") if t>u else print ("U")
# APPARENTLY AND CAN BE USED
q=75
z=64
c=56
if q>z and q>c :
    print("q is greater than z and c")
    # there's also or, not, 
    #Nested if
    v=10
    p=12
    if v>p:
        print ("v is greater than p")
        if p>v :
          print("p is greater than v")
        else: 
            print ("null")
#loops : while and for loops
#while loops
"""
i=1
while i< 6:
    print (i)
    i+=1
    """
# break statement
i=1
while i < 6:
        print(i)
        if i == 3:
            break
        i +=1
    
# the countinue statement
i=1
while i < 6:
          print
          if i ==3:
               continue
          print (i)
# the else statement
i=1
while i>6:
     print(i)
     i += 1
else: 
     print ("i is no longer less than 6")
     #program prints grades






