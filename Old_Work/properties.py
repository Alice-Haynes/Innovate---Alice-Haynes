import random
# import the random library 

# the following both do the same thing... HASHED OUT LINES 6 TO 14

# import random
# print(random.random())
# print(random.uniform(1, 10))
# print(random.randint(1,10))

# from random import random, randint, uniform
# print(random())
# print(uniform(1, 10))
# print(randint(1,10))

print("Hello World")
# outputs hello world
print(len("hello world"))
print(len("1234"))
# outputs the length of the string, including spaces
print("alice haynes"[3])
# outputs the specified index in string, remembering index from [0]
print("All Around the World"[7].upper())
# outputs the specified index in uppercase
print(random.random())
# generates a random number between 0 and 1, including 0 and excluding 1
print(random.uniform(1, 10))
# generates a random number between 1 and 10, inclusive.
print(random.randint(1,100))
# generates a random INTEGER between 1 and 10, inclusive.

# ACTIVITY 1 - Create the grid using only the print method.

print("   |   |   ")
print("   |   |   ")
print("   |   |   ")
print("-----------")
print("   |   |   ")
print("   |   |   ")
print("   |   |   ")
print("-----------")
print("   |   |   ")
print("   |   |   ")
print("   |   |   ")

# ACTIVITY 2 - Look into these methods write an example of each with an explanation of how each one works:

print("ALICE HAYNES".lower())
# .lower - makes occurences lowercase
print("hello".upper())
# .upper - makes occurrences uppercase
print("hello".capitalize())
# .capitalize - makes occurrences start with a capital letter
print("Alice Haynes".count("e"))
# .count - gives a count of how many times an occurrence occurs
print("alice haynes".find("e"))
# .find - finds the index of the character or starting index of a word
print("alice haynes".replace("alice haynes","Miss A S Haynes"))
# .replace - replace an occurrence with an alternative ("old one","new one")
print("alice sarah haynes".strip("alicynes"))
# removes from the left and right any charachter specified before blocked by unspecified characters
print ("     alice   sarah haynes   ".strip())
# also used to remove additional spacing (think annoying email input on phone sign up) still only left and right


# ACTIVITY 3 - use another random method. Are there other useful methods… from built-in library? ..from random library? https://docs.python.org/3/library/random.html
 
print(random.randrange(6, 20))
# randrange generates a random integer between a set range, 6 and 20, not including 20.
