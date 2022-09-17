

# Ask user to enter their age
# print out your age is {age}
# till their age gets to 60
# print("Enter your current age")
# age = int(input())

# # Their age should be smaller equal to 60

# while age <=60:
#     print(f"Your age is {age}")
#     age+=1




# Ask user to enter two numbers, first is greater than the second one. 
# Find out sum of all the numbers between given two numbers not inclusive. 3
# first number is 7
# second number is 3
#  4 5 6  -> 15 
# first number is 9
# second number is 6
# 6    7 8     9  -> 15
# first num 11
# second num is 7
# # 7    8 9 10     11 -> 27 
# print("Enter a number")
# num1 = int(input())
# print("Enter a number smaller than first one")
# num2 = int(input())

# #Before we get to the sum let's print all the numbers between given two number
# copyOfnum2 = num2
# num2 = num2 +  1
# sum = 0
# while num2 < num1:
#   #  print("In the loop",num2)
#   sum += num2
#   num2 = num2 +1
# print(f"Sum of the numbers between {num1} and {copyOfnum2} is {sum}")  



# Prime number
# prime numbers can only be divided by 1 and itself.
# Every number can be divided by 1 and itself but prime numbers cannot be divisible 
# by any other number than 1 and itself.
# for example:
# 3 can only be divided by 1 and 3
# 7 can only be divided by 1 and 7
# 11
# 13
# 19
# 17
# 23 is prime
# You should ask user to give a number
# Find out if the given number is prime number or not prime number. 

# The given should not be divided by any other number than 1 and itself
# I have to check all the numbers that is smaller than given number to see
# if they can divide the given number.

# 18 is it possible divide 18 with the number bigger than 18

# print("Enter a number")
# num = int(input())

# I have to start checking from possible divisors
# What is the smallest number that you can divide the non prime numbers other than 1?
# 2
# 12 % 2 == 0
# Using break statement we can stop the loop regardless of the condition.
# How can I print when the number is a prime? 

# To understand if the number is a prime we should check all possible divisors 
# and see none-of them can divide the number
# on the line below i assume the given number is prime
# is_prime = True
# possible_divisor = 2
# while possible_divisor < num:
#     if num % possible_divisor == 0:
#         #When this if statement gets executed it means given number is not prime
#         #Whenever this if statements gets executed I don't have to check rest of the 
#         # possible divisors to understand if it is a prime
#         # How can I tell the code given number is not prime?
#         is_prime = False
#         # If you understand the number is not prime no need to continue to rest of the loop
#         break
#     possible_divisor+=1   

# if is_prime:
#     print("this is a prime number")
# else:
#     print("This is not a prime number")


# print("Enter your current age")
# age = int(input())
# # Their age should be smaller equal to 60
# while age <=60:
#     print(f"Your age is {age}")
#     age+=1



# Break 

# break statement is used to stop loop from continuing.

# We use the loops for certain purpose 
# and if we can understand no need for iterating we can stop the code using break statement. 

# Syntax -> break

# Right after the break statement we cannot insert a code 

# while 3<4:
# 	print("3 is smaller than 4")
# 	break
# ------------------------------------------------

# num1 = 5
# num2 = 6
# while True:
# 	if num2 < num1:
# 		print("num2 is less than num1")
# 		break
# 	else:
# 		print("num2 is not less than num1")
# 		break

# --------------------------------------------------------------



# num1 = 1
# while True:
# 	if num1 % 7 == 0:
# 		print("Num1 is divisible by 7")
# 		break
#     num1+=1
# 	print(num1)
# # What will be the value of num1?
# 7
# -----------------------------------------------------------
# Flags in python
# We create a boolean condition before the loop and assumme 
# True or False. In the loop we change this condition to 
# use outside to loop again. 

# Ask user to enter a string
# if the given string contains any duplicated letter
# print string has duplicated letter 
# otherwise print string consists of unique letters. 

# print("Enter a string")
# str = input()

# # we should check for each letter, if there is duplication
# is_unique = True
# index =0
# while index<len(str):
#     if str.count(str[index])>1:
#         # it means there is duplicated letter
#         is_unique = False
#         break
#     index+=1

# if is_unique==True:
    
#     print("String consists of unique letters")
# else:
#     print("String has duplicated letters")    


# range function in python

# Range is one of the built in functions in python

# syntax -> range(5)
# this will give you numbers between 0 and 4 inclusive

# You can also choose where do you want range function to start

# range(1,6)
# This will give you numbers between 1 and 5 inclusive

# You can also give incrementing step for range function
# range (3,12,2)
#  THis will give you 3 5 7 9 11

# range (3,12,3)
# This will give you 3 6 9 

# Range function will only work with integer numbers.

# print(type(range(5)))
# # What do you think the output will be?
# It will be range class. range function returns a range object.

# for x in range(2,21,2):
#     print(x)


# Iterable objects in python are range,strings, tuples, 
# lists and arrays
# Which means they can be used with for loop and we can iterate in
# individual elements from them. 

# #For Loop
# It works with iterable objects and gets individual elements
# from iterable objects and allow us to modify the 
# individual objects.

# str = "Techtorial"

# #Print each letter from str 
# for l in str:
# 	print(l)
# 	print(type(l)) # String

# for x in range(5):
# 	print(x) 

# # 0 1 2 3 4 

# # Print all the even numbers from 2 to 20 inclusive
# for x in range(2,21,2):
# 	print(x)
# # 2 4 6 8 10 12 14 16 18 20

# # Print all the even numbers from 2 to 20 inclusive
# # Without using step in the range function
# for x in range (2,21):
# 	if x % 2 ==0:
# 		print(x)


