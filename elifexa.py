print("Enter any number")
num1 = int(input())

print("Enter any number")
num2 = int(input())

print("Enter any number")
num3 = int(input())

# Print first number is bigger than second if the num1 bigger than num2
# print num1 and num2 equal to each other if they are equal

if num1>num2 :
    print("first number is bigger than the second number")
elif num1==num2:
    print("Both numbers have the same value.")

# elif statement gets only executed when the previous conditions are false

# Print first number is bigger than second if the num1 bigger than num2
# Print second number is equal number 3 if the num3 equal num2

if num1>num2 :
    print("first number is bigger than the second number")
elif num2==num3:
    print("Both num2 and num3 have the same value.")

# THe elif condition above will only work when the first if statement is not executed



if num1>num2 :
    print("first number is bigger than the second number")
if num2==num3:
    print("Both num2 and num3 have the same value.")

# THe two if conditions above do not have any effect on each other