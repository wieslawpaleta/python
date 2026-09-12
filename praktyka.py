#Praktyka W3Schools
#Python Introduction, Getting Started, Syntax, Statements, Syntax Code Challenge, Output / Print, Numbers, Output Code Challenge, Comments, Challenge: Comments,
#Variables, Variable Names, Variables - Assign Multiple Values, Output Variables, Global Variables, Variable Exercises, Variables Code Challenge,
#Data Types, Data Types Code Challenge, Numbers, Numbers Code Challenge, Casting,  Casting Code Challenge, Strings, Slicing Strings, Modify Strings
#  

import sys
import random


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


# x = ""
# print(type(x))
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
x = frozenset({"cheese", "mouse", "rat"})
print(type(x))
x = True
print(type(x))
x = b"Hello"
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
print(type(x))
x = None
print(type(x))

print("\n")

x = str("Goodday")
print(type(x))
x = int(20)
print(type(x))
x = float(10.09)
print(type(x))
x = complex(5j)
print(type(x))
x = list(("cheese","mouse","rat"))
print(type(x))
x = tuple(("cheese","mouse","rat"))
print(type(x))
x = range(3)
print(type(x))
x = dict(food="cheese", type="tasty")
print(type(x))
x = set(("cheese", "mouse", "rat"))
print(type(x))
x = frozenset(("cheese", "mouse", "rat"))
print(type(x))
x = bool(5)
print(type(x))
x = bytes(5)
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
print(type(x))


x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


print(random.randrange(1, 10))


x = int(1)
y = int(2.8)
z = int("3")


x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")


x = str("s1")
y = str(2)
z = str(3.0)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

print(a[1])

for x in "kingdom":
    print(x)

print(len(a))

print("Lorem" in a)

if "Lorem" in a:
    print("Yes, 'Lorem' is there.")

print("Deliverance" not in a)

if "Deliverance" not in a:
    print("No, 'Deliverance' is NOT present.")


b = "Penguins go 'uhuhu'"
print(b[2:5])

print(b[2:])

print(b[-5:-2])

print(b.upper())

print(b.lower())

print(b.strip())

print(b.replace("U", "A"))

print(b.split(" "))

#  String Concatenation, Format - Strings, Escape Characters, String Methods  (Teraz tu jestem!)
#
#
#
#


a = "Peguins "
b = "go 'uhuhu'"
c = a + b
print(c)

a = "Peguins"
b = "go 'uhuhu'"
c = a + " " + b
print(c)


age = 60
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} euros"
print(txt)

txt = f"The price is {20 * 59} euros"
print(txt)

txt = "We\t are\b\rso-called \"Vikings\" \\from\n the\f north." 
print(txt)