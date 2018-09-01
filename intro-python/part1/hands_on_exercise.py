"""Intro to Python - Part 1 - Hands-On Exercise."""
""" code by myounker 1 Sep 2018 """


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(type(pi))
print(pi)

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50:
    print('i is less than 50! i = ', i)
elif i == 50:
    print ('i is 50! i = ', i)
else:
    print ('i is greater than 50! i = ', i)


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == 'orange':
    print('orange was selected and this is the color orange')
elif picked_fruit == 'strawberry':
    print('strawberry was selected and this is the color red')
elif picked_fruit == 'banana':
    print('banana was selected and this is the collor yellow')
else:
    print ('none of the 3 fruits matched. error!')


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def mult(num1, num2):
    result = num1 * num2
    return result

# TODO: Now call the function a few times to calculate the following answers
print("12 x 96 =", mult(12, 96))
print("48 x 17 =", mult(48, 17))
print("196523 x 87323 =", mult(196523, 87323))
