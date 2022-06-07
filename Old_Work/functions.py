
# create or define function
def press_grind_beans():
    print("Grind beans for 20 seconds.")

# execute or run function
press_grind_beans()

# EXAMPLE 1

def say_hello():
    print("Ex1 - Hello")

say_hello()

# EXAMPLE 2

w_amount = 100
account_num = 123457

def cash_withdrawal(amount, accnum):
    print(f"Ex2 - Withdrawing £{amount} from account {accnum}.")

cash_withdrawal(500, 123456)
cash_withdrawal(w_amount, account_num)

# variables that are created outside of a function are known as GLOBAL VAIABLES. Global variables can be used by everyone both inside and outside of a function. When you create a variable inside a function it is a local function unless otherwise stated.

# EXAMPLE 3

def coffee_order(cup_size, type):
    print(f"Ex3 - I'll have a {cup_size} {type}.")

coffee_order("large", "latte")

# EXAMPLE 4

def add_up(num1, num2):
    return num1 + num2

print(add_up(5, 2))

# EXAMPLE 5

# converts celsius to fahrenheit
def multiply_by_nine_fifths(celsius):
    return celsius * (9/5)
def get_fahrenheit (celsius):
    return multiply_by_nine_fifths(celsius) + 32

print("Ex5a - The temperature is {}°F".format(get_fahrenheit(15)))

#converts fahrenheit to celsius
def minus_32(fahrenheit):
    return fahrenheit - 32
def get_celsius (fahrenheit):
    return minus_32(fahrenheit) * (5/9)

print("Ex5b - The temperature is {}°C".format(get_celsius(59)))

# https://www.webnots.com/alt-key-windows-shortcuts/ - for shortcuts to symbols!

# ACTIVITY 1 - Here's an example of a function that includes a parameter. Parameters are responsible for functions being able to work on different data inputs. Edit the snippet below to include two or more parameters and a running order count updated when the function is called:

# order_count = 0

# def take_order(size, topping, base):
#     global order_count
#     print(f"Ac1 - I'll have a {size} pizza with {topping} on a {base} base.")
# def order_counts:(order_count)
#     order_counts =+ 1
#     print(f"order number{order_counts}")
    
# take_order("small", "mushrooms", "thin crust")




# ACTIVITY 2 - Cash machine time. Let’s create one that: 

    # - Takes an input of pin number and amount
    # - Prints dispensing cash if the pin number is correct and there’s enough money to withdraw
    # - Displays the new bank balance
    # - Be creative!

    #def transaction(pin_number, amount):
    
