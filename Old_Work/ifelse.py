# EXAMPLE 1

music = ""

if music == "classical":
    print("Oh no it's that classical again")
elif music == "no music":
    print("Arh peace and quiet")
else:
    print("Nice and noisy")

# EXAMPLE 2

age = 16

if age > 17:
    print("Yes I can serve you")
else:
    print("You aren't old enough.")

# EXAMPLE 3

place = "MCR"
weather = ""

if place == "MCR" and weather == "sunny":
    print("Check again")
elif place == "MCR" and weather == "rain":
    print("Obvs")
else:
    print("What.. it isn't raining?")

# EXAMPLE 4

age = 18
country = "uk"

if age > 17 and country.lower() == "UK":
    print("Yes I can serve you")
elif country.lower() != "UK":
    print("What country are you in?")
else:
    print("You aren't old enough.")

# EXAMPLE 5

day = "Monday"

if day == "saturday" or day == "sunday":
    print("It's the wekend!")
else:
    print("When's it weekend?")

# CHALLENGE 1 - Create a variable called password. Check how many letters are in the password, if there  are less than 8 print that the password is too short. Otherwise print the password.

password = "catcat"

if len(password) < 8:
    print("password is too short")
else:
    print(password)

# CHALLENGE 2 - Create a variable called num. Check if the variable is divisible by 3 or 5. If it is print  “This number is divisible by 3 or 5” to the console. Otherwise log “This number is not divisible by 3 or 5”.

num = 21

if num%3 == 0 or num%5 == 0:
    print("This number is divisible by 3 or 5")
else:
    print("This number is not divisible by 3 or 5")

# CHALLENG 3 - Create a variable called num. If num is divisible by 3 print “fizz”, if it’s divisible by 7  print “buzz”, if it’s divisible by both 3 and 7 print “fizz buzz”. Otherwise print num.

num = 21

if num%3 == 0 and num%7 != 0:
    print("fizz")
elif num%3 != 0 and num%7 == 0:
    print("buzz")
elif num%3 == 0 and num%7 == 0:
    print ("fizz buzz")
else:
    print(num)

# CHALLENGE 4 - Create a variable called word that takes a string.  Create an if statement that checks if the last letter is  the same as the first. If it is return true, otherwise  return false.

word = "treat"

if (word[0]) == (word[((len(word))-1)]):
    print("True")
else:
    print("False")

word = "treat"

if (word[0]) == (word[-1]):
    print("True")
else:
    print("False")

# CHALLENGE 5 - Create a variable called time, a variable called  place_of_work and a variable called town_of_home.  Create an if statement that prints where someone is  at times of the day. E.g. if the time is 7 I’m at home, at  8 I’m commuting, at 9 I’m at work.

time = 9
place_of_work = "work"
town_of_home = "Ashton"

if time == 7:
    print(f"Im at home in {town_of_home}")
elif time == 8:
    print(f"I'm commuting between {town_of_home} and {place_of_work}.")
elif time == 9:
    print(f"I'm in {place_of_work} working.")
else:
    print("They are lost!")

# CHALLENGE 6 - Create two variables called num1 and num2. Create an if statement that checks if the result of the  sum is even. If it is, return a success message.

num1 = 4
num2 = 4

if (num1 + num2)%2 == 0:
    print("winner!")
else:
    print("try again")

# ACTIVITY 7 - Create a variable called num. Check if the number is a palindrome (looks the sameforward as it does backwards e.g. 1001 or 20202).

num = "703542625307"

if (num) == (num[::-1]):
    print(f"{num} is a palindrome!")
else:
    print(f"{num} is no palindrome")

# ACTIVITY 8 - Take the string "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi”.Find the index of a last vowel in the string.

bab = "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi"
bab_len = (len(bab))
bab_back = bab[::-1]
i_a = bab_len -1- bab_back.find("a") 
i_e = bab_len -1- bab_back.find("e") 
i_i = bab_len -1- bab_back.find("i")
i_o = bab_len -1- bab_back.find("o")
i_u = bab_len -1- bab_back.find("u")
list1 = [i_a, i_e, i_i, i_o, i_u]
# print(i_a)
# print(i_e)
# print(i_i)
# print(i_o)
# print(i_u)
#print(bab_back)
#print(bab_len)
print("The index of the last vowel is", max(list1))




