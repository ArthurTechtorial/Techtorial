



# Create a program that will ask user ten full name 
# After you get 10 full name create email version of given 10 
# name and store it inside list and print. 
#enter fullname
# John Wick
#enter fullname
# Max White

#["johnwick@gmail.com","maxwhite@gmail.com",.....]



# full_names = []
# emails = []

# for i in range(10):
#     print("Enter a full name")
#     f_name = input()
#     full_names.append(f_name)
#     f_name = f_name.replace(" ","").lower()+"@gmail.com"
#     emails.append(f_name)

# print(full_names)
# print(emails)

# Sets
# ___________________________________________________

# Sets are used to store multiple 
# elements in a single variable.
# Sets are unordered objects so sets don't use 
# indexing.
# We can only store immutable objects in the set. 
# Sets do not allow duplicate values. 

# Syntax
# _____________________________________________________

# set = {value1,value2,value3}
# Using set() function we can convert list in to sets. 
# set = {}
# print(type(set)) <class 'dict'>
# There for to create an empyt list we use set function
#  s = set()


# set = {1,3,10,9,1}

# print(set)

# It will throw an error
# print(set[0])

# Set itself is mutable object but we cannot store mutable object in
# a set.
# string, boolean, integer,float are immutable
# list is mutable

# It will throw an error
# set1 = {1,9,3,4,[3,456,6,7]}


# We use two methods to remove elements from the set.
# discard() method and remove() method. 

# remove(valueOfTheObject)

# set = {3,5,7,9}

# # I want to remove the number 7 from the set. 

# set.remove(7)
# # number 7 will be gone from the set. 
# print(set)

# # when the element needs to be removed does not exist in the set
# # it will throw an error.
# # set.remove(7)

# # discard(valueOfTheObject) method

# set.discard(3)
# print(set)
# # when the element needs to be removed does not exist in the set
# # it will not throw an error and it won't anything.
# set.discard(3)



# s = set()

# print(type(s)) # set
# print(s)
# s.add("new value")

# print(s)

# s = {} # dict

# print(type(s))

# # using set() function we can convert lists in to set
# # How we can remove the duplicates from the list below?
# list = ["s","s",2,2,4,5,7,3,6,3,2]

# set1 = set(list)
# print(set1)
# print(type(set1)) # set


# copy method
# list = ["s","s",2,2,4,5,7,3,6,3,2]

# set1 = set(list)
# print("From line 31",set1)

# set2 = set1.copy()
# print(set1 == set2)
# print("set 2 from line 35",set2)
# print(type(set2)) # set
# 3:26
# # clear()
# set1.clear()


# There are some methods we can compare two sets with each other. 

# s1 = {1,7,9,3}

# s2 = {2,7,9,5}
# # difference method will get the elements present 
# # in set, that is not present in the other set.
# print(s1.difference(s2)) # {1,3}

# print(s2.difference(s1)) # {2,5}

# # What do you think the return type of difference method? 
# print(type(s2.difference(s1))) # <class 'set'>

# # Intersection
# s1 = {1,7,9,3}

# s2 = {2,7,9,5}
# # Intersection method will return elements that are present in the 
# # both sets. 
# print(s1.intersection(s2)) #{9, 7}
# print(type(s1.intersection(s2))) # <class 'set'>


# #issubset()
# # It check given set is present in the other set or not. 
# set = {1,2,3,4,5}
# set2 = {2,3,4}
# # Since all elements of the set2 is in the set
# # set2 is subset of the set . 

# print(set2.issubset(set)) # True
# print(set.issubset(set2)) # False

# #issuperset()
# # If the set has all the elements of an other set, it is called 
# # superset.
# # set is a superset of the set2
# print(set.issuperset(set2)) # True
# print(set2.issuperset(set)) # False



# # intersection_update
# # It will remove all the elements that are not present in the 
# # other set
# # intersection_update doesn't have a return type. 
# s1 = {1,2,3}

# s2 = {2,3}
# s1.intersection_update(s2)
# print(s1)

# s2.intersection_update(s1)
# print(s2)

# # difference_update,
# # When it is used it will remove the 
# # common elements of two sets 
# s1 = {1,2,3}

# s2 = {2,3}
# # difference update method doesn't have a return type. 
# s1.difference_update(s2)
# print(s1)

# print(s2)

# s3 ={1,2,3}
# s2.difference_update(s3)

# print(s2)  # empty set

# Is set object is iterable ? 
# set objects are iterable. 
# s1 = {"new","value2","value3","value4"}

#  # Sets don't have index numbers. 

# for element in s1:
#     print(element)

# # String is an iterable object 
# # string is ordered, so it has index numbers .
# str = "Python"
# s2 = set(str)

# print(s2)  # {'n', 't', 'h', 'o', 'y', 'P'}
# print(str) # Python

# # If you want to get first element from the str ? 
# print(str[0])  # P

# # If you want to get first element from the list? 
# #print(s2[0]) #it will throw an error

# index = 0
# while index < len(str):
#     print(str[index])
#     index+=1

# for x in str:
#     print(x)

# for element in s2:
#     print(element)

# # This line will throw an error because we cannot use 
# # index numbers with set.
# # index =0
# # while index < len(s2):
# #     print(s2[index])

# # len()

# print(len(s2)) #It will print the size of s2 which is a set






# Given two lists a, b. Check if two lists have 
# at least one element common in them.

# Examples:

# Input : a = [1, 2, 3, 4, 5]
#         b = [5, 6, 7, 8, 9]
# Output : True

# Input : a=[1, 2, 3, 4, 5]
#         b=[6, 7, 8, 9]
# Output : False


# list1 = [1, 2, 3, 4, 5]

# list2 = [ 6, 7, 8, 9]

# # Check if two lists have 
# # at least one element common in them.

# set1 = set(list1)
# set2 = set(list2)

# # How can i check if there is common element from these two sets? 
# # In the below i will get common elements from both sets above.
# common_elements = set1.intersection(set2)

# # If there is at least one common element what should be the size of 
# # common_elements set?
# # It should be at least 1.
# # len(common_elements) >= 1

# # if len(common_elements) >=1:
# #     print("True")
# # else:
# #     print("False")

# is_there_common = len(common_elements) >= 1

# print(is_there_common)


# s  = {2,2,3,4,5,7}
# s2 = {4,10,2,5,44}
# print(min(s))
# print (max(s2))
# print(min(s)*max(s2))
# # find out min number from the s and 
# # multiply with the max number of s2
# min = -200
# max1 = 0 
# #In the first iteration of the loop i should 
# # change the value of the min but later on I should only change 
# # it when the min is bigger than the number
# # in the loop below how can I understan it is the first iteration
# count_of_iteration = 0
# for number in s:
#     if count_of_iteration == 0:
#         min = number
#         max1 = number
#     if number < min:
#         #If code comes to this line it means min is bigger than number
#         min = number
#     elif number > max1:
#         max1 = number    
#     count_of_iteration+=1  
   


# print("This is the min from the second first set",min)
# print(max1)


# max =0
# for number in s2:
#     if max == 0:
#         max = number
#     if max < number:
#         max = number

# print ("This is the maximum from the second set",max)    

# print("Multiplication of min and max is", min*max)

