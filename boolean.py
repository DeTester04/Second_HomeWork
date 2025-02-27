#Boolean Values

print(10 > 9)   #True
print(10 == 9)  #False
print(10 < 9)   #False


#Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  #b is not greater than a

#Evaluate Values and Variables
#The bool() function allows you to evaluate any value, and give you True or False in return,

#Evaluate a string and a number:

print(bool("Hello")) #True
print(bool(15)) #True

#Evaluate two variables:

x = "Hello"
y = 15

print(bool(x)) #true
print(bool(y)) #true

