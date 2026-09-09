#Praktyka W3Schools
#Python Introduction, Getting Started, Syntax, Statements, Syntax Code Challenge, Output / Print, Numbers, Output Code Challenge, Comments, Challenge: Comments,
#Variables, Variable Names, Variables - Assign Multiple Values, Output Variables, Global Variables, Variable Exercises, Variables Code Challenge,
#Data Types  (Teraz tu jestem!)

import sys


print("Gooday!\n")
print(sys.version)


x = 5
y = "Ball"


if x != y:
    print("\nHow are you?")


print(x * y)


print("I haven't known"); print("that"); print("it is possible!")
print("Double quotes"); print("Single quotes")


print("I have keys but open no locks.I have space but no room.You can enter, but you can't go outside. What am I?", end=" ")
print("A computer keyboard.")
print(1)
print("I am", 1000, "years old.")
print(1 + 1000)


"""
This is a multiline comment,
but you will not see it, right?

"""


z = str(3)
w = int(3)
u = float(3)


print(type(z))
print(type(w))
print(type(u))


zupa = "zupa"
apuz = 'zupa'
print(zupa + " = " + apuz)


p = "rower"
P = 0
print(p)
print(P)


myvar = "Grzyb"
my_var = "Grzyb"
_my_var = "Grzyb"
myVar = "Grzyb"
MYVAR = "Grzyb"
myvar2 = "Grzyb"
myVarName = "Grzyb"
MyVarName = "Grzyb"
my_var_name = "Grzyb"
myvar = "Grzyb"


x, y, z = "Castle", "Stronghold", "Fortress"
print(x)
print(y)
print(z)


x = y = z = "Citadel"
print(x)
print(y)
print(z)


buildings = ["Castle", "Stronghold", "Fortress"]
x, y, z = buildings
print(x)
print(y)
print(z)


x = "Python is a duck"
print(x)


x = "Python"
y = "is"
z = "a duck"
print(x, y, z)


x = "Python "
y = "is "
z = "a duck"
print(x + y + z)


x = 0
y = 1
print(x + y)


x = 5
y = "Geese"
print(x, y)


x = "Python"

def myfunc():
    print("Python is " + x)


myfunc()


x = "Python"

def myfunc():
    global x
    x = "nohtyP"
    print("Python is " + x)


myfunc()


#-----------------


x = ""
print(type(x))
x = "Goodday"
print(type(x))
x = 20
print(type(x))
x = 10.09
print(type(x))
x = 5j
print(type(x))
x = ["cheese","mouse","rat"]
print(type(x))
x = ("cheese","mouse","rat")
print(type(x))
x = range(3)
print(type(x))
x = {"food" : "cheese", "type" : "tasty"}
print(type(x))
x = {"cheese", "mouse", "rat"}
print(type(x))
x = ""
print(type(x))
x = ""
print(type(x))
x = ""
print(type(x))
x = ""
print(type(x))
x = ""
print(type(x))
x = ""
print(type(x))
x = ""
print(type(x))
