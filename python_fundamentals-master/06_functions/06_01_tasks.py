'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results


# num divisible by 4 OR 7
def my_bool(num):
    if num % 4 == 0 or num % 7 == 0:
        return bool(True)
    else:
        return bool(False)


z = my_bool(9)
print(z)


# num divisible by 4 AND 7

def my_bool1(num):
    if num % 4 == 0 and num % 7 == 0:
        return bool(True)
    else:
        return bool(False)


z = my_bool1(28)
print(z)

# pass user input through a function

user_in = int(input("Enter a number between 1 and 1,000: "))

a = my_bool(user_in)
b = my_bool1(user_in)

print("The number entered is divisible exactly by either 4 OR 7: " + str(a))
print("The number entered is divisible exactly by both 4 AND 7: " + str(b))




