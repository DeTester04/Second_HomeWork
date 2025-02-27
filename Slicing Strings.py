# Slice From the Start

## By leaving out the start index, the range will start at the first character:

### Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5]) #Hello

# Slice To the End

## By leaving out the end index, the range will go to the end:
### Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:]) #llo, World!

# Negative Indexing

## Use negative indexes to start the slice from the end of the string:

### Get the characters:

#From: "o" in "World!" (position -5)

#To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2]) #orl