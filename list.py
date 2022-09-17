




# list = [2,3,5,True,"s"]

# print(len(list))# 5

# print(list[4]) # s

# print(type(list)) #<class 'list'>

# print(type(list[3])) #<class 'bool'>

# print(type(list[4])) # <class 'str'>
# print(type(list[2])) #<class 'int'>

# # Slicing the list
# print(list[1:4]) # [3, 5, True]
# print(type(list[1:4])) # <class 'list'>

# print(list[0:3]) # [2, 3, 5]
# print(type(list[0:3])) # <class 'list'>

# print(list[:2]) # [2,3]
# print(list[2:]) # [5,True,'s']

# Using in operator we can specified value is in the list or not.
# We can also use in operator for strings as well.

# list =[1,2,3,4,5]

# if 2 in list:
#     print("2 is in the list ")

# if 11 in list:
#     print("11 is in the list.") # This lline will not work because
#     # 11 is not in the list .

# # not in operator will check if the specified value is not in the 
# # iterable objects. 

# if 6 not in list:
#     print( 6, "is not in the list")



# # Using in operator we can specified value is in the list or not.
# # We can also use in operator for strings as well.

# list = [1,2,3,4,5]

# if 2 in list:
#     print("2 is in the list ")
# if 11 in list:
#     print("11 is in the list.") # This lline will not work because
#     # 11 is not in the list .
# # not in operator will check if the specified value is not in the 
# # iterable objects. 
# if 6 not in list:
#     print( 6, "is not in the list")

# ask user to enter a random digit 
# check if the digit is present in our list or not.
# if user enters present element print you won a prize,
# if not, print maybe, next time. 
# print("Enter a random digit")
# digit = int(input())

# if digit in list:
#     print("You have won a prize")
# elif digit not in list:
#     print("Maybe, next time.")



# list = ["Python","C++","C#","Java","Ruby"]

# # Remove the C# from the list? 

# list.remove("C#")

# print(list) #["Python","C++","Java","Ruby"]

# #["Python","C++","Java","Ruby"]

# # I want to remove the second element from this list.

# list.pop(1)
# print(list)
# #['Python', 'Java', 'Ruby']

# # since the -5 is not in the list it will give index error
# # list.pop(-5)
# # print(list)
# #Index out ouf range error
# #list.pop(12)

# # If you use bigger or lower indexes to get elements from iterable 
# #objects you will index out of range error. 
# #print(list[20])




# nums = [1,2,3,4,5,6,7]

# nums.pop(5)

# print(nums) #

# #[1, 2, 3, 4, 5, 7]
# nums.remove(5)
# print(nums)

# # nums.remove(5)

# # print(nums)


# nums = [1,2,3,5,4,5,6,7]

# # It will remove the first 5 that exist in the list. 
# nums.remove(5)

# print(nums)

# nums.clear()

# print(nums)


# ist = ["s1",'s2',"s3"]

# for el in list:
#     print(el)

# for index in range(len(list)):
#     print(list[index])


# nums = [1,2,3,1,2,3,4,2,2,2]


# # Remove all the number 2's from this list.
# # First I can find count of 2's in the list 
# # I can apply the remove method count times.
# count = 0
# for number in nums:
#     if number == 2:
#         count+=1
# print(count)
# # i need to apply the remove method count times
# # i need to crete a loop that iterates count times

# #How many times the loop will get executed?
# #It will get executed count times
# for i in range(count):
#     nums.remove(2)
# print(nums)



# nums = [1,2,3,1,2,3,4,2,2,2]


# # Remove all the number 2's from this list.

# # I can create a copy of this list
# newList = nums.copy()

for number in newList:
    if number == 2:
        nums.remove(2)
print(nums)



# nums = [1,2,10,11,13,17,21,26]

# #From the given list find sum of all the even numbers 
# # lets find sum of all the odds seperately
# sum = 0
# sum_odd = 0
# for number in nums:
#     if number % 2 == 0:
#         sum += number
#     else:
#         sum_odd += number

# print("Sum of all the even numbers from list is",sum)
# print("Sum of all the odd numbers is",sum_odd)



# list =[1,5,6,11,90,3,6]

# #Print all the odd numbers from index number 3 to 6 inclusive


# # I need an index number that is ranging from 3 to 6 inclusive

# for index in range(3,7):
#     if list[index] % 2 !=0:
#         print(list[index])



