
# Question-1

# s=""

# print("Enter a text:")

# text=input()

# length=len(text)-1

# while length>=0:
#     s=s+text[length]
#     length-=1

# print(s)


#Question-2


# print("Enter your minimum number:")

# min=int(input())

# print("Enter your maximum number:")

# max=int(input())

# total=0

# while min<=max:
#     if min%3==0 and min%11==0:
#         total+=min
#     min+=1
# print(total)


# Question-3


# print("Enter a number between including 1 to 9")

# between=int(input())
# output=str(between)
# for n in range(1,between):
#     output+=str(between)

# print(output)



#Question-4

# print("Enter a number between including 1 to 9")

# goingdown=int(input())
# output=""
# while goingdown>0:
#     for n in range(0,goingdown):
#         output+=str(goingdown)
#     print(output)
#     output=""
#     goingdown-=1

        
# Question-5

# print("Enter a text")

# stri = input()
# letters = []

# for i in stri:
#     if i not in letters or i == " ":
#         letters.append(i)
# print("".join(letters))


print("Please enter one string")
str=input()
str=str.removeprefix(" ").removesuffix(" ")

new_version=""

index=0
while index<len(str):
    if str.count(str[index])==1:
        new_version=str.count(str[index])
    index+=1
    print(new_version)

# Question-6




