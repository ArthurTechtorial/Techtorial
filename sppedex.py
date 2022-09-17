


# getting ticket for speed violation
#   in state of IN, speed limit on HighWays is 70
#   in other states, speed limit on Highways is 55
#   -if driver exceeds speed limit for up to 10% of the limit in each state, 
#    we will give WARNING in that state
#     state of IN warning means --> print --> "YELLOW WARNING"

#     other state warnings mean --> print --> "CITATION"
# -if driver exceeds speed limit more than 10% of the limit in each state,
#  we will give TICKET in that state
#     state of IN ticket means --> print --> "$150 and 5 points"
#     other state warnings mean --> print --> "$100"
# -if speed is same as  speed limit, --> print --> "You are driving safe!"


# getting ticket for speed violation
#   in state of IN, speed limit on HighWays is 70  78
#   in other states, speed limit on Highways is 55
#   -if driver exceeds speed limit for up to 10% of the limit in each state, 
#    we will give WARNING in that state
#     state of IN warning means --> print --> "YELLOW WARNING"

#     other state warnings mean --> print --> "CITATION"
# -if driver exceeds speed limit more than 10% of the limit in each state,
#  we will give TICKET in that state
#     state of IN ticket means --> print --> "$150 and 5 points"
#     other state warnings mean --> print --> "$100"
# -if speed is same as  speed limit, --> print --> "You are driving safe!"

speed_limit_IN, speed_limit_others = 70,55

print("What speed are you travelling at the moment?")
speed_of_driver = int(input())

print("What state are you in at the moment?")
state_in = input()

#If the condition below is True driver is in IN 
#If the driver is not in indina the condition below will be False
is_in_IN = state_in =="IN"
#print(not is_in_IN)

ten_percent_up_IN = speed_limit_IN + speed_limit_IN*10/100

ten_percent_up_Others = speed_limit_others + speed_limit_others*10/100

if is_in_IN and speed_of_driver<=speed_limit_IN:
    print("You are driving safe!")
elif is_in_IN and speed_of_driver>speed_limit_IN and speed_of_driver<=ten_percent_up_IN:
    print("YELLOW WARNING")   
elif is_in_IN and speed_of_driver > ten_percent_up_IN:
      print("$150 and 5 points")
elif not is_in_IN and speed_of_driver<=speed_limit_others:
     print("You are driving safe!")
elif not is_in_IN and speed_of_driver>speed_limit_others and speed_of_driver<=ten_percent_up_Others:  
    print("CITATION")
elif not is_in_IN and speed_of_driver>ten_percent_up_Others:
    print("$100")











