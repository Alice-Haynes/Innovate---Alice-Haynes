
from datetime import datetime
from lib2to3.pgen2.token import NAME

my_name = "Alice Haynes"
my_age = 36
student = True
student = False
print (my_name)
fav_drink = "Hot Chocolate"
print ("My favourite drink is", fav_drink)
print ("My favourite drink is {}".format(fav_drink))
print ("{}'s favourite drink is {}".format(my_name,fav_drink))
print (f"{my_name}'s favourite drink is {fav_drink}")
print ("Alice \"monster\" Haynes")

i = 10
i = i + 2
print(i)
j = 11
j += 3
print(j)
print ("")

# ACTIVITY 1 - Create a program that stores someone’s name, age and favourite colour that prints these in a complete sentence.

name = "Alice"
age = 36
color = "Green"
print (f"My name is {name} and i am {age}. My favourite colour is {color}")

# ACTIVITY 2 - Create a program that stores what you eat today for breakfast, lunch and dinner, print these. Update each of these variables to what you will eat tomorrow, print these.

breakfast = "toast"
lunch = "soup"
dinner = "pizza"

print (f"Today I will have {breakfast} for breakfast, I will have {lunch} for lunch and then I will have {dinner} for dinner.")

breakfast = "cereal"
lunch = "a sandwich"
dinner = "spag bol"

print (f"Tomorrow I will have {breakfast} for breakfast, I will have {lunch} for lunch and then I will have {dinner} for dinner.")

# ACTIVITY 3 - (1) Create a 9 variables space1, space2… space9 (2) Assign either the value "x", "o", " " to each of these variable (3) Insert the variables into the board using the {} .format() syntax and make your board look like the one displayed.

box_1 = "x"
box_2 = "o"
box_3 = " "
box_4 = "x"
box_5 = "x"
box_6 = " "
box_7 = "o"
box_8 = " "
box_9 = " "

print("   |   |   ")
print(f" {box_1} | {box_2} | {box_3} ")
print("   |   |   ")
print("-----------")
print("   |   |   ")
print(f" {box_4} | {box_5} | {box_6} ")
print("   |   |   ")
print("-----------")
print("   |   |   ")
print(f" {box_7} | {box_8} | {box_9} ")
print("   |   |   ")

# ACTIVITY 4 - Research into all operators mentioned in this session, give an example of each.

i = 10
# sets i as 10
print(i)
# prints 10
i *= 5
# processes i and multiplies it by 5
print(i)
# prints 50
i += 6
# adds 6 to i, noting i is continuing to update
print(i)
# prints 56
i /= 7
# divides i by 7
print(i)
# prints 8
i -= 3
# minuses 3 from i
print(i)
# prints 5

# ACTIVITY 5 - Create a program that calculate the number of days from today to your birth date, and print this out.

import datetime

todays_date = datetime.date.today()
next_birthday = datetime.date(2022, 9, 7)
# print(todays_date)
# print(next_birthday)
print((next_birthday) - (todays_date))


