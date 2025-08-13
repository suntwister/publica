# 1

# # Collecting user favourite dishes
# dish_1 = input("Enter your first favourite nigerian dish: \n")
# dish_2 = input("Enter your second favourite nigerian dish: \n")
# dish_3 = input("Enter your third favourite nigerian dish: \n")
# print("----------------------")
# # converting inputs to list
# list1 = [dish_1, dish_2, dish_3]

# # converting list to tuple
# dishes = tuple(list1)

# print("\n".join(dishes))

# 2
# # Collecting user best friends names
# friend_input = input("Enter your best five friends seperated by space: \n").split()

# # converting friends name input to tuple
# friend = tuple(friend_input)
# print("----------------------")
# # output of turple in reverse order
# print(friend[::-1])

# 3
# Collecting user 5 Nigerian states
user_states = input("Enter five Nigerian states seperated by space: \n").split()

# converting user states input to tuple
states = tuple(user_states.title() for user_states in user_states)
#output
print("--------------------------------------------")
print(f'\t first state: {states[0]} \n\t second state: {states[-1]}')
print("--------------------------------------------")
print("Is there Lagos in tuple:\t", ("YES") if "Lagos" in states else ("NO"))
print("--------------------------------------------")
print("The number of states entered is: ", len(states))
print("--------------------------------------------")

# 4 
# Collecting user profiles
user_name = input("Enter your first name: \n")
user_age = input("Enter your age: \n")
user_color = input("Enter your favorite color: \n")
user_town = input("Enter your home town: \n")
# adding inputs to list and converting to tuple
list2 = [user_name, user_age, user_color, user_town]
user_profile = tuple(list2)
