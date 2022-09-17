
# Print numbers from 1 to 10 inclusive
# num =1
# while num<=10:
#     print(num)
#     # I have to update the value of variable num in the loop so 
#     # condition will become false eventually. 
#     num = num + 1
# print(f"Value of the variable num is {num}") # 11
# # Print even numbers that are smaller equal to 10
# num = 2
# while num <= 10:
#     print(num)
#     num = num + 2
# print(f"Value of the variable num is {num}") # 12


# # Print even numbers that are smaller equal to 10
# # This time variable num is going to start from 1
# num = 1
# while num <= 10:
#     if num%2==0:   # This line is in the while loop
#         print(num) # This line is in the while as well as in the if statement   
#     num +=1        # This line is in the while loop

# #Line below is there for to understand what value the variable num will take 
# # after the loop above.
# print(num) # 11

# From 1 to 20 inclusive, print every odd number in following format
# "This is an odd number {Value of number}"
# print every even number 
#"This is an even number {Value of number}"

# num = 1
# while num <=20:
#     #In the while loop I have to decide num is currently even or odd
#     if num % 2==1:                               #This line is in only while loop
#         print(f"This is an odd number {num}")    #This line is in while loop also in if
#     else:                                        #This line is in only while loop
#         print(f"This is an even number {num}")   #This line is in while loop also in if
#     #I have to update the value of the number
#     num +=1                                      #This line is in only while loop 

#Example of an infinite loop.
# num =0
# while num < 1:
#     print("in the while loop")                     #This line is in the while
# print("Outside the while after the infinite loop")  #This line is outside the while



# # Ask user to give you a string
# # From that string print index numbers of all the e's
# #  
# print("Enter a text")
# str = input()

# # We can access string elements using their indexes.
# index = 0

# # Index number is always smaller than length of the string.
# #"Example"
# # 0123456  Index numbers
# #   7  Length of the string
# length_of_str = len(str)

# while index < length_of_str:
#     # I want to acces the element with index number str[index]
#     if str[index] == "e":
#         print(f"Index number of e is {index}")
#     index+=1

# account=40
# remaining_calls=account//5
# calls=0
# while account>=5:
#     account-=5
#     remaining_calls-=1
#     calls+=1
#     print(f"You made {calls} calls.")
#     print(f"You can make {remaining_calls} calls")
#     print(f"Remaining money {account}$")

print("Enter a number")
n=int(input())
i=1
divisorno=0
print (f"Divisors of {n} are as follows:")
while i<=n:
    if n%i==0:
        divisorno+=1
        print (f"Divisor {divisorno} is ",i)
    i+=1




