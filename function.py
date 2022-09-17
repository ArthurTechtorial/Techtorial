



# def print_name():
#     print("Techtorial")

# print_name()

# def print_greeting(name):
#     print(f"Hello {name}")


# print_greeting("Arthur")



# def get_greeting(name):
#     return f"Hello {name}"


# print(type(get_greeting("Arthur")))
# print(get_greeting("Arthur"))
# print(get_greeting("Steven"))

# def sum(num1,num2):
#     addition = num1 + num2
#     s     = str(type(addition))
#     if "int" in s or "float" in s:
#         return addition
#     else:
#         return "An error occured."

#     # if type(num1 + num2)
#     # return 
# # Methods will always stop when the code reaches the return statement. 

# print(sum("A","B"))
# print(sum(1,3))


def sum2(*nums):
    sum=0
    for element in nums:
        sum+=element
    return sum


print(sum2(1,5,21,54,66))
