

#Question-1

# s1="Snicker"

# s1=s1.upper()

# print(s1)

# s1=s1.removeprefix("S")

# print(s1)

# s1=s1.strip("RE")
# print(s1)


# s2="Cookie"

# s2=s2.lower()

# print(s2)

# s2=s2.replace("o","u")

# print(s2)


# s2=s2.removesuffix("e")

# print(s2)


# s2=s2.replace("c","C")

# print(s2)
 

#Question-2
# print("Enter a text including spaces")

# s3=input()

# s3=s3.replace(" ", "")


# length=len(s3)

# if length%2 == 0:
#     print("False")
# else :
#     print("True")

#Question3

# print("Enter any three-word-text")

# s4=input()

# s4split=s4.split()
# print(s4split)


# s4split1=len(s4split[0])-1
# s4split2=len(s4split[1])
# s4split3=len(s4split[2])
# secondindex=s4split1+s4split2+1
# thirdindex=s4split1+s4split2+s4split3+2
# print ("Index of first word\'s last index is", s4split1)
# print ("Index of second word\'s last index is", secondindex)
# print ("Index of third word\'s last index is", thirdindex)
# print("The sum is" , s4split1+secondindex+thirdindex)

#Question 4

# print("Enter a song name")
# song=input()

# firstletter=song[0]
# indexlong=len(song)-1
# lastletter=song[indexlong]
# kfind=song.find("k")

# print(firstletter)
# print(lastletter)
# print(len(song))
# print(kfind)
# print(song[3])
# print(song.upper())
# print(song.lower())

#Question5

# print("Please enter three ingridients with spaces:")
# s=input()
# s=s.split()
# print(s)
# s1=s[0]
# s2=s[1]
# s3=s[2]

# print("Please enter a number:")
# n=int(input())
# print(s1,s2,s3)


# f1=s1[0]
# f2=s2[0]
# f3=s3[0]

# s1=str(n)+s1.removeprefix(f1)
# n=n+1
# s2=str(n)+s2.removeprefix(f2)
# n=n+1
# s3=str(n)+s3.removeprefix(f3)


# print(s1,s2,s3)

#Question 6

# print("Enter a text")
# text=input()

# print("The text you entered will be starting from the number you entered:")

# start=int(input())

# print("The text will end at the number you entered:")

# end=int(input())

# cut=text [(start-1):end]

# print(cut)


Question-7

print("Enter a random text")

random=input()
print("How many letters or spaces your text consist of?")
entry=int(input())
print(entry==len(random))

print("Which letters index do you want to learn?")

query=input()

found=random.find(query)

print(found)
















