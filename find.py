



# s1="java"

# print(s1.find("va"))


# #    012345
# s = "Python"

# print(s.find('y')) # 1

# print(s.find("o")) # 4
# #     012345678
# s1 = "Java Java"
# print(s1.find("a")) # 1 

# # When we use multiple charachters in find method 
# # it finds that sequence and returns the index of first charachter
# print(s1.find("va")) # 2 

# print(s1.find("al")) # -1 

# print(s1.find("z")) #  -1 
# # Index of first a present in the string
# print(s1.find("a")) #1 
# # what if I want to find index of last a present in the string? 

# print(s1.rfind("a")) # 8 because index of last a present in the string

# # index of last a present in the string means same as highest index number of a 

# # I want to find index of second a present in the string 

# # I can find the lowest index for a True
# lowest_a = s1.find("a") #1
# #"Java Java"[2:] -> va Java

# s1_newVersion = s1[lowest_a+1:]
# #"va Java"
# index_of_second_a = s1_newVersion.find("a")+ lowest_a+1


# print(f"index of second a is {index_of_second_a}")










