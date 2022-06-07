### PART 1 ###

##! BASICS

greeting = "hello world"
print(greeting)

print(len(greeting))
# to get length of string
print(greeting[4])
# to get specified character *count starts from 0*
print(greeting.upper())
# turns string to uppercase
print(greeting.lower())
# print(greeting.lower())
print(greeting.capitalize())
# print(greeting.capitalize())

# print(greeting.find())
# print(greeting.replace())
# print(greeting.strip())

##! LIBRARIES

import random
print(random.random())
print(random.uniform(1, 10))
print(random.randint(1,10))
# OR
from random import random, randint, uniform
print(random())
print(uniform(1, 10))
print(randint(1,10))

##! VARIABLES

greeting = "hello"
print(greeting, "it's nice to meet you!")
# OR
greeting = "hello"
print(greeting + " there, nice to meet you!")
# OR
greeting = "hello"
print("{} there, nice to meet you!" .format(greeting))
# OR
greeting = "hello"
print(f"{greeting} there, nice to meet you!")

##! INPUT

response = input("How would you like to respond? \n")
print(f"How did the user respond?: \n'{response}'")

##! IF ELSE

music = "classical"
if music == "classical":
    print("Oh no! It's classical music again.")
elif music == "no music":
    print("Ahh, peace and quiet!")
else:
    print("Nice and noisy.")

place = "MCR"
weather = "Cloudy"
if place == "MCR" and weather == "Sunny":
    print("Check again")
elif place == "MCR" and weather == "Rain":
    print("Obvs")
else:
    print("Wait, it isn't raining?")

age = 20
country = "UK"
if age > 17 and country == "UK":
    print("Yes I can serve you")
elif age > 17 and country != "UK":
    print("Where are you?")
else:
    print("You aren't old enough")

day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("When's the weekend?")

##! FUNCTIONS

def cash_withdrawal(amount, accnum):
    print(f"Withdrawing {amount} from account {accnum}")
cash_withdrawal(300, 50449921)

w_amount = 100
account_num = 12345678
def cash_withdrawal(amount, accnum):
    print(f"Withdrawing {amount} from account {accnum}")
cash_withdrawal(w_amount, account_num)
cash_withdrawal(300, 50449921)
cash_withdrawal(30, 50449921)

# LISTS

#.remove()
#.reverse()
#.sort()
#.count()
#.extend()

# FOR LOOPS / WHILE LOOPS



##! ACTIVITY 1
# Create variable that holds the text “Welcome to Code Nation”.
# Find the length of the string and save this to a new variable.
# Create a function that checks if the string length is even;
# if it is, print the string, the length and an appropriate message in one sentence.
# Do the same but with a different message if it’s odd.
# Change the string length so you can test all possible outcomes.

var = "Welcome to Code Nation"

var_len = len(var)
#print(var_len)

var_len_ev = ((var_len) %2)
#print(var_len_ev)

if (var_len_ev) == 0:
    print(f"{var} has {var_len} characters, meaning it has an even number length.")
else:
    print(f"{var} has {var_len} characters, meaning it has an odd number length.")

##! ACTIVITY 2
# Create a list that represents the alphabet: alphabet = ["a", "b", "c", "d"...
# Create a for loop to iterate through this and print each letter in order.
# Now using input, allow the user to type a number and print the letter it represents in the alphabet.
# Remember how index works - and think about how to structure your code.

##! ACTIVITY 3
# Remember the noughts and crosses activity? Let’s revisit that and start to improve with our improved knowledge.
# Create a structure of functions that allow the player to play against the computer - here is a suggestion:
# Function to start the game, let player choose ‘0’ or ‘X’.
# Function to print the board & show the player how to choose spaces.
# Function for the player to choose their space.
# Function for the computer to take its turn.
# Function to check the logic of if there’s a win, lose or draw after every turn is taken.


### PART 2 ###

##! CONVERTING DATA TYPES

#--> int() - creates an integer data type
int(5.4) # Expected: 5 ** ROUNDS DOWN **
int("54") # Expected: 54
#int("hello world") # Expected: ValueError: invalid literal for int() with base 10: 'hello world’
#--> float() - creates a floating point data type
float(54) # Expected: 54.0
float("54") # Expected: 54.0
#--> str() - creates a string data type
str(54) # Expected: 54
str(54.0) # Expected: 54.0

##! TRUTHY AND FALSY

# Empty string ""
# Integer value 0
# Floating point value 0.0
# Everything else is Truthy 

print("What is your name?")
name = input()
if name:
    print(f"Hello {name}, how are you?")
else:
    print("You did not give me your name!")

##! NOT OPERATOR

print(not True) # Expected: False
print(not False) # Expected: True



    
