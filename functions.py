#learn functions in python
"""
just like in c++ functions are a block of code used to perform a particular task
aruguments are information about the function passed into the psrenthesis
"""
def firstfunction():
     print ("hello this is my first function")
firstfunction()

"""
  
def namefunction(fname):
     print (fname + "Refsnes")
namefunction("Emil")
namefunction("Quinn")
   
"""

def newfunction(fname, lname):
     print(fname+ " " +lname)
newfunction("emil", "quinn")

  
def dara(age, course):
     print(age+ " " +course)
dara("16", "s.w.e")


def my_function():
      print("my name is darasimi")
my_function()

def got():
     print ("i think i see it now")
got()
      
def house(love, tears):
     print(love+ " "+tears)
house("i love it when the sky xries", "i can hear the brids playing the flute")

def poem(violin, viola):
     print(violin+ " "+viola)
poem("they make the rain sound magical", "the thuder become an ember than an asunder")

def thelittleprince(stars, oldman):
     print(stars+ " "+oldman)
thelittleprince("look at one star you'll hear me laughing in another i'll be laughting too", "it'll be as if all the stars are laughing if you listen closely")

def arbitary(*argument):
     print("the youngest child is " + argument[0])
arbitary("quinn", "nester")

def arbitary(*nanny):
     print("it is only with the eye " + nanny[0])
arbitary("once can see nothing", "the in essential", "nothing")

def arbitary(*biebie):
     print ("it is only with the heart one can see " + biebie[3])
arbitary("what is essential", "nothing", "darkness", "what is essential")

def keyword(dara1):
     print("darasimi's first child's name is " + dara1)
keyword(dara1="I-Conquer")

def keyword(dara2):
     print("darasimi's second child name is "+ dara2)
keyword(dara2="I-Saw")

def keyword(dara3):
     print ("darasimi's third child name is "+ dara3)
keyword(dara3="I-Came")

def keyword(**dara1):
     print ("the possible names for darasimi's first child is "+ dara1["name"])
keyword(name="Aniale",name2= "Aimer", name3="Aderioan", name4="Alexander", name5="Adenuga", name6="Adeaie")

def default(name = "dara"):
     print("my name is " + name)
default("Duanougha")
default("Dgounga")
default("howare")

def dara(name="2"):
     print("My no.1 position is the " + name)
dara("1")
dara("3")

#passing a list as an argunment
def list(name):
     for x in name: #syntax for list in string
          print(x)
name = ["dasiey", "daisty", "hunter"]
list(name)

def breast (nook):
     for v in nook:
          print(v)
nook=["book", "cook", "sook"]
breast(nook)

def fish (garden):
     for d in garden:
          print(d)
garden = ["jardin", "jade", "juine"]
fish(garden)

def beer (bees):
     for x in bees:
          print(x)
bees = ["hornet", "honey bee", "wild bee"]
beer (bees)

def function(e):
     return 5 * e
print (function(3)) 

def function(i):
     return 6 * i
print(function(5))
print (function(3))

# positional arguments
def position(o, /):
 print(o) 
position (3 )
def positions(h, /):
     print(h)
positions (5)

def keyarguments(*, d):
     print (d)
keyarguments(d=3) # remeber the diffrence between arguments and keywords arguments is that the former does not have assigned values while the lattter can have assigned values

#combine positional-only and keyword only
def colmbination(a, b, /, *, c, d):# these are parameters
     print(a + b + c + d)
colmbination(3, 5, c= 0, d= 4 ) # these are the arguments:the values passed in function when called

def colmbination (s, /, *, t):
     print (s*t)
colmbination(3, t=2)

def colmbination (i,k,/,*,f,h):
     print (i+k+f+h)
colmbination(2,3, f=6,h=5)

#recursion
# writing code recursively with (-8)
