
# ###! DAY 2 - D1.P2 CONTINUED ###

# #! TRY/EXCEPT

# def add_up():
#     num1 = input("What is the first number you'd like to add up? \n")
#     num2 = input("What is the second number you'd like to add up? \n")
#     try:
#         print(f"{num1} + {num2} is {(int(num1) + int(num2))}!")
#     except:
#         print("\n ERROR: please input only numerical values. \n")
#         print("**************************** \n")
#         add_up()
# add_up()

# def add_up():
#     num1 = input("What is the first number you'd like to add up? \n")
#     num2 = input("What is the second number you'd like to add up? \n")
#     try:
#         print(f"{num1} + {num2} is {(int(num1) + int(num2))}!")
#     except:
#         print("\n ERROR: please input only numerical values. \n")
#         print("**************************** \n")
#         add_up()
# add_up()

# #! SCOPE - GLOBAL AND LOCAL VARIABLES

# light = False

# def light_switch():
#     global light
#     if light:
#         print("Whoa! It’s bright in here")
#         light = False
#     else:
#         print("Who turned out the lights?")
#         light = True

# light_switch()
# light_switch()

# def show_num():
#     num = 13
#     print(num)
# num = 10
# show_num()

# #! LISTS / TUPLES

# even_nums = [2, 4, 6, 8, 10] # [] is a list - mutable (changed)
# odd_nums = (1, 3, 5, 7, 9) # () is a tuple - unmutable (unchangeble)

# even_nums[-1] = "ten"
# #odd_nums[-1] = "nine" # throws error

# #! SLICE NOTATION

# # - my_list[start:stop] - Specify the start and stop index
# # - my_list[start:] - Specify the start index,slice until the end of list
# # - my_list[:stop] - Slice from the start of list, specify the stop index
# # - my_list[:] - Copy the list

# #! LOOPS - WHILE TRUE

# while True:
#     print("Run forever")

# loop_runs = True
# while loop_runs:
#     print("Run the loop!")
# #Do something...
#     loop_runs = False
# #To stop the loop


# #! BREAK AND CONTINUE

# while program_is_running:
#     if condition_is_met:
#         continue
#     else:
#         break

###! ACTIVITY 1 ###

# Create a program with an input variable that encourages the user to enter a number into the terminal.
# If they do, have the program convert this into the Int data type, and show me the evidence.
# If they don’t, print a ‘try again’ message.
# Break down this challenge into your own terms, and use research to help you solve it.
# Look back through the Python recap and this presentation to see what syntax you can use to help you do this.

def response():
    num = input("Please pick a number. \n")
    try:
        {num} is {(int(num))}
        print("Your number is an integer!")
    except:
        print("\n ERROR: try again. \n")
        response()
response()

###! ACTIVITY 2 ###

# We are going to make a program inspired by the film Ghostbusters using IMBD as your main source of research.
# This is an open-ended activity and there’s bonus points for creativity.
# Will you have a list of cast members? 
# A function that randomly gives you a quote from the movie?
# A while loop trivia game that only stops once you get a question right? 
# Go through the key concepts to make sure you’re practicing these and your evidencing understanding of them.

#CAST Bill Murray, Dan Aykroyd, Harold Ramis, Ernie Hudson, Sigourney Weaver, Rick Moranis, Annie Potts

q1 = input("What was the green blob called?\n")
if q1 == "Slimer":
    print("Correct!")
elif q1 == "slimer":
    print("Correct!")
else:
    print("Wrong!")

q2 = input("Who Played Peter Venkman? \n")
if q2 == "Bill Murray":
    print("Correct!")
elif q2 == "bill murray":
    print("Correct!")
else:
    print("Wrong!")

# age = 20
# country = "UK"
# if age > 17 and country == "UK":
#     print("Yes I can serve you")
# elif age > 17 and country != "UK":
#     print("Where are you?")
# else:
#     print("You aren't old enough")

# day = "Saturday"
# if day == "Saturday" or day == "Sunday":
#     print("It's the weekend!")
# else:
#     print("When's the weekend?")

