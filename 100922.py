




# Ask user to enter a positive integer number 
# Check if the given number is within 2 of a multiple of 10 . 
# If it is within 2 of a multiple 10 print 
# Your number is within 2 of a multiple 10 
# If not print your number didn't match the expected requirement. 

# 10 -  20 - 30 - 40 - 50 -> so on
# IF the user gives 21 -> your number is within 2 of a multiple 10 
# if the user gives 43 -> your number is within a multiple 10 
# if the user gives 39 -> your number is within 2 of a multiple 10
# We need to use remainder operator.

# If the given number remainder with 10 is less than equals to 2 
# It means it is withing 2 of a multiple 10
# 11 % 10 -> 1 
# 22 % 10 -> 2 
# 30 % 10 -> 0 

# 9 ->     10
# 18 ->    
# If the also given number remainder with 10 is bigger or equal to 8 
# The given number is within 2 of a multiple 10


   #                     8 9 10 11 12
   #                   38 39 40 41 42


# print("Enter a positive integer number")
# num = int(input())

# remainder = num % 10 

# if remainder>=8 or remainder<=2:
#     print("your number is within 2 of a multiple 10")
# else:
#     print("your number didn't match the expected requirement. ")   



# Ask user to give you two integer numbers. 
# Find the sum of these two integer numbers. 
# If sum of these two integer is smaller than 10 
# print sum of these two numbers is 10 
# if sum of these two number is between 10 - 19 inclusive, 
# print sum of these two numbers is 20
# For all other conditions 
# print the actual sum of these two numbers. 

# print("Enter first number")
# num1 = int(input())
# print("Enter second number")
# num2 = int(input())

# sum = num1  +  num2

# if sum < 10:
#     print("sum of these two numbers is 10")
# elif sum>=10 and sum<=19:
#     print("sum of these two numbers is 20")
# else:
#     print(f"sum of these two numbers is {sum}") 



# The doctors say you babies can go out in summer if the weather is 
# between 60 and 80 inclusive.If not they say you shouldn't take the baby out. 
# In the winter they say you can go out if the weather is hotter than -20
# . Ask user what season they are in also ask user how hot the weather 
# is  and print if they can go out with baby or not. 

# print("What season are you in?")
# season = input()

# print("How hot is the weather?")
# w = int(input())

# # if user enters SuMMEr
# if season.lower() =="summer":
#     #If this line is getting executed, it means season is summer.
#     if w<=80 and w>=60:
#         print("You can take the baby out.")
#     else: 
#          print("You shouldn't take the baby out.")
# elif season.lower() =="winter":
#     if w > -20:
#         print("The babies can go out.")
#     else:            
#          print("You shouldn't take the baby out.")





#Ask user to enter a date in format of month/day/year
#                                       mm/dd/yyyy
# Convert given date like following examples
# 03/06/2017      -> March 6, 2017
#      -4-3-2-1
# 07/10/2022      -> July 10, 2022

# print("enter a date in format of month/day/year, mm/dd/y ")
# #                                       mm/dd/yyyy")

# date = input()
# # First two charachters of the given date will give you the number of month
# month = date[0:2]
# day   = date[3:5]
# year  = date[-4:]
# # In which conditions should I modify the date? 
# # When the date is starting with 0, I should remove the 0
# day= day.removeprefix("0")

# if month == "01":
#     print(f"January {day}, {year}")
# elif month == "02":
#      print(f"February {day}, {year}")
# elif month == "03":
#      print(f"March {day}, {year}")
# elif month == "04":
#      print(f"April {day}, {year}")
# elif month == "05":
#      print(f"May {day}, {year}")
# elif month == "06":
#      print(f"June {day}, {year}")
# elif month == "07":
#      print(f"July {day}, {year}")
# elif month == "08":
#      print(f"August {day}, {year}")
# elif month == "09":
#      print(f"September {day}, {year}")
# elif month == "10":
#      print(f"October {day}, {year}")
# elif month == "11":
#      print(f"November {day}, {year}")
# elif month == "12":
#      print(f"December {day}, {year}")



# In the factory we need to create a program that can 
# find if we can do the shipment and if we can do the shipment
# it will tell use how many small package we should ship.
# First we need to get total kilogram of the shipment,
# to reach this total kilogram of shipment we can use small and big packages. 
# Every big package is 5 kilogram and every small packages is 1 kilogram.
# We have limited amount of small and big packages. 
# Ask user how many big and how many small package  they have.
# Ask user what is the total goal kilogram of the shipment.
# Print whether they can ship, if they can ship print how many small packages they need. 
# Assume big packages is used before small packages. 

# count of small package = 4 -> 4 kilogram
# count of big package = 1 -> 5 kilogram 
# goal is to ship 9 kilogram 
# i can ship and i need to use 4 small package

# 5 small package-> i need to use 3 smal package
# 4 big package  -> how many big package i need to use -> 2
# I need to ship 13 kilogram 
# i can ship and i need to use 3 small package

# 3 small package-> i need to use 4 small package to complete but since i don't 
# have 4 small package i cannot ship
# 3 big package -> i can use max 2 big package
# i need ship 14 kilogram
# I cannot ship

# print("Enter the kilogram we need to ship")
# goal_ship = int(input()) # 12

# print("Enter amount of small packages you have")
# count_of_small = int(input())

# print("Enter amount of big packages you have")
# count_of_big = int(input())

# # I have to start from big packages to reach goal kilogram
# # How can I find how many big package i need to reach to goal?

# needed_big_packages = goal_ship // 5


# # If I don't have enough big packages can I do the shipment-No

# # 9 small package
# # 1 big package 
# # I need to ship 14 kilogram
# if needed_big_packages<=count_of_big:
#     #How many small package i need
#     needed_small_packages = goal_ship%5
#     if needed_small_packages <= count_of_small:
#         print(f"I can do the shipment and i need {needed_small_packages} amount of small package")
#     else:
#         print("I cannot do the shipment")
# else:
#     # How many kilogram can I reach with the big boxes i have  and then the rest of the amount i will 
#     # try to complete with using small packages
#     kilogram_i_have = count_of_big * 5;
#     left_goal = goal_ship - kilogram_i_have
#     # Left goal divided by 1 will give amount of small package i need 
#     if left_goal<=count_of_small:
#         print(f"I can do the shipment and I need {left_goal} amount of small boxes")
#     else:
#         print("i cannot do the shipment.")




print(“Enter an integer number”)
num1 = input()
print(“Enter an integer number”)
num2 = input()
sum = int(num1) + int(num2)
if sum < 10 :
    print(“sum of these two number is 10")
elif sum >= 10 and sum <= 19:
    print(“sum of these two numbers is 20”)
else:
    print(sum)





