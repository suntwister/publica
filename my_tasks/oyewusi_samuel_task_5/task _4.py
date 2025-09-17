
# 4 
# Collecting user profiles
user_name = input("Enter your first name: \n").title()
user_age = input("Enter your age: \n")
user_color = input("Enter your favorite color: \n").title()
user_town = input("Enter your home town: \n").title()
# adding inputs to list and converting to tuple
list2 = [user_name, user_age, user_color, user_town]
user_profile = tuple(list2)
converting tuple to variable
users = str(user_profile)
print("----------------------------------")
print(f"First name:\t | {user_name}")
print(f"Age:    \t | {user_age}")
print(f"Favorite color:\t | {user_color}")
print(f"Home town:\t | {user_town}")
print("----------------------------------")
