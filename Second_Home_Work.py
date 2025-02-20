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

#variable names:

#myvar = "Mary"
#my_var = "John"
#_my_var = "John"
#myVar = "John"
#MYVAR = "John"
#myvar2 = "John"

#values to multiple variables in one line
x, b, z = "Orange", "Banana", "Cherry"
print(x)
print(b)
print(z)

#And you can assign the same value to multiple variables in one line:

x = f = z = "Orange"
print(x)
print(f)
print(z)

#If you have a collection of values in a list, tuple

fruits = ["apple", "banana", "cherry"]
x, p, z = fruits

print(x)
print(p)
print(z)

#The Python print() function is often used to output variables.

x = "Python is awesome"
print(x)

#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
d = "is"
z = "awesome"
print(x, d, z)


#You can also use the + operator to output multiple variables:

x = "Python "
p = "is "
z = "awesome"
print(x + p + z)

#For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

x = 5
y = "John"
print(x, y)