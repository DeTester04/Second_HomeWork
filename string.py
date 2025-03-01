#Strings are Arrays
#Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1]) #e

#Looping Through a String
#Since strings are arrays, we can loop through the characters in a string, with a for loop.

#Loop through the letters in the word "banana":

for x in "banana":
  print(x)

#String Length
#To get the length of a string, use the len() function.

a = "Hello, World!"
print(len(a))

#Check String
#To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("free" in txt)

#Use it in an if statement:
#Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
#Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)

#Use it in an if statement:

#print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

