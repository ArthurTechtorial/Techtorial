num1= 5
num2= 7

if num1 < num2:
    print(f"{num1} is less than {num2}")    
#
# What is the result of num2 < num1 -> False 
if num2 < num1:
    print(f"{num2} is less than {num1}")  # This line will not get printed

# If statement will execute the next line only when the given condition is 
# True.
is_num2_bigger = num2 > num1

if is_num2_bigger:
    print("num2 is bigger than num1")

# Ask user to enter a string
# if user enters a string with all lower cases print you entered correct cases 
print("Enter a string")
str = input()
is_Lower = str.islower()

if is_Lower:
    print("You entered correct cases ")    # 1
    print("because you entered all lower") # 2
print("you entered a string ")             # 3

#Line number 1 and 2 is inside the if statement so they depend on condition, but 
# line number 3 is outside the if statement (because no indentation) therefore, 
#line number 3 doesn't depend on any condition.