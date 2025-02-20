
#Variables of numeric types are created when you assign a value to them:

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

#Integers:

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#Float

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#Complex

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#Convert from one type to another

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

