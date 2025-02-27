# First_Test
Confix Hub

1. # Python Variables

x = 5
y = "John"
print(x)
print(y)


y = 4
x = "Sally"
print(x)

#x = str(3)    # x will be '3'
#y = int(3)    # y will be 3
#z = float(3)  # z will be 3.0

x = 5
A = "John"
print(type(x))
print(type(A))

# 2.Python - Variable Names

#variable names:

#myvar = "Mary"
#my_var = "John"
#_my_var = "John"
#myVar = "John"
#MYVAR = "John"
#myvar2 = "John"

## Multi Words Variable Names

Camel Case
Each word, except the first, starts with a capital letter:
myVariableName = "John"

Pascal Case
Each word starts with a capital letter:
MyVariableName = "John"

Snake Case
Each word is separated by an underscore character:
my_variable_name = "John"


# 3.Python Variables - Assign Multiple Values

## Many Values to Multiple Variables

#values to multiple variables in one line
x, b, z = "Orange", "Banana", "Cherry"
print(x)
print(b)
print(z)

## And you can assign the same value to multiple variables in one line:

x = f = z = "Orange"
print(x)
print(f)
print(z)

## If you have a collection of values in a list, tuple

fruits = ["apple", "banana", "cherry"]
x, p, z = fruits

print(x)
print(p)
print(z)

# **4.Python - Output Variable**

## The Python print() function is often used to output variables.

x = "Python is awesome"
print(x)

## In the print() function, you output multiple variables, separated by a comma:

x = "Python"
d = "is"
z = "awesome"
print(x, d, z)


## You can also use the + operator to output multiple variables:

x = "Python "
p = "is "
z = "awesome"
print(x + p + z)

## For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

## The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

x = 5
y = "John"
print(x, y)

# 5 Python Global Variables

## Create a variable outside a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

## Create a variable inside a function, with the same name as the global variable

x = "awesome"  # This is a global variable

def myfunc():
  x = "fantastic"  # This is a local variable inside the function
  print("Python is " + x)  # This prints: "Python is fantastic"

myfunc()  # Calling the function

print("Python is " + x)  # This prints: "Python is awesome"

## If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x  # Declares 'x' as a global variable
  x = "fantastic"  # Assigns the string "fantastic" to 'x'

myfunc()  # Calls the function to execute the code inside it

print("Python is " + x)  # Prints "Python is fantastic"

## To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)

# Setting the Data Type

## In Python, the data type is set when you assign a value to a variable:

x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memory view (bytes(5))	memory view	
x = None	NoneType	

# Setting the Specific Data Type

## If you want to specify the data type, you can use the following constructor functions:

x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memory view(bytes(5))	memory view	

# Python Numbers

## There are three numeric types in Python:

int
float
complex

Variables of numeric types are created when you assign a value to them:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

## Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

Example
Integers:

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


## Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

Example

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


# Complex numbers are written with a "j" as the imaginary part:

Example
Complex:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion

## You can convert from one type to another with the int(), float(), and complex() methods:

Example
Convert from one type to another:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Slice From the Start

## By leaving out the start index, the range will start at the first character:

### Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5]) #Hello

# Slice To the End

## By leaving out the end index, the range will go to the end:

Example

### Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:]) #llo, World!

# Negative Indexing

## Use negative indexes to start the slice from the end of the string:

Example

### Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2]) #orl

# Python - Modify Strings

## Upper Case

### The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

# Lower Case

## The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())

# Remove Whitespace

## Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

### The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


# Replace String

## The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

# Split String

## The split() method returns a list where the text between the specified separator becomes the list items.

### The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Python - String Concatenation

# String Concatenation

### To concatenate, or combine, two strings you can use the + operator.

### Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c) #HelloWorld

To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c) #Hello World

# Python - Format - Strings
## As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

Create an f-string:

age = 36
txt = f "My name is John, I am {age}"
print(txt)

# Placeholders and Modifiers
## A placeholder can contain variables, operations, functions, and modifiers to format the value.
### Add a placeholder for the price variable:

price = 59
txt = f "The price is {price} dollars"
print(txt)

# A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal 
formatting type, like .2f which means fixed point number with 2 decimals:

## Display the price with 2 decimals:

price = 59
txt = f "The price is {price:.2f} dollars"
print(txt)

# Perform a math operation in the placeholder, and return the result:

txt = f "The price is {20 * 59} dollars"
print(txt)

# Boolean

## Most Values are True

## Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

Example
The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

