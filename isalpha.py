


# isalpha() method
# It only returns true when all charachter of the string is letters .

s = "This is text"
print(s.isalpha()) 
# False and the reason for that is spaces are not considered as letters. 

# s = s.replace(" ","")
print(s.replace(" ","").isalpha())
#True because using replace method we removed all the spaces from the string.

print(s.replace(" ","-").isalpha())
# IT will print False because - is not a letter.

print(type(s.isalpha())) # class<bool>

# isnumeric() only returns true when all the charachters are numeric 

s1 = "777-777-7777"
print(s1.isnumeric())
#False because - is not a numeric type.

print(s1.replace("-","").isnumeric())
# True
s1 = "7777b4eh3"
print(s1.isnumeric())
# It will return False
print(s1.isalnum()) # True
# isalnum checks if the all string consist of letters and numbers

print(s1.isalnum())
#It will True
s1 = "777-777-7777"

print(s1.isalnum())
#False because it has - 
# It doesn't have to contain both letter and number at the same time.
# even it has only one of the type it will return True
s2 = "String"
s3 ="777777"
s4 = "478eiuHjr847iu"
s5 ="ksjadl45-"
print(s2.isalnum())   # True
print(s2.isnumeric()) # False
print(s2.isalpha())   # True
################################
print(s3.isalnum())   # True
print(s3.isnumeric()) # True
print(s3.isalpha())   # False
################################
print(s4.isalnum())   # True
print(s4.isnumeric()) # False
print(s4.isalpha())   # False
################################
print(s5.isalnum())   # False
print(s5.isnumeric()) # False
print(s5.isalpha())   # False




















