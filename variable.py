

# Python Variables

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
j = 10
print(x + j)

## The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

x = 5
c = "John"
print(x, c)


## Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


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