
# # 4 
# # Collecting user profiles
# user_name = input("Enter your first name: \n").title()
# user_age = input("Enter your age: \n")
# user_color = input("Enter your favorite color: \n").title()
# user_town = input("Enter your home town: \n").title()
# # adding inputs to list and converting to tuple
# list2 = [user_name, user_age, user_color, user_town]
# user_profile = tuple(list2)
# converting tuple to variable
# users = str(user_profile)
# print("----------------------------------")
# print(f"First name:\t | {user_name}")
# print(f"Age:    \t | {user_age}")
# print(f"Favorite color:\t | {user_color}")
# print(f"Home town:\t | {user_town}")
# print("----------------------------------")

# 5
shop_list1 = input("Enter first item for shopping: \n").title()
shop_list2 = input("Enter second item for shopping: \n").title()
shop_list3 = input("Enter third item for shopping: \n").title()

# converting shop lists input to tuple
tuple_list = (shop_list1, shop_list2, shop_list3)

# coverting tuple to list
shop_list = list(tuple_list)

# Adding more items
print("Enter two more items: ")
shop_list4 = input("Enter fourth item for shopping: \n").title()
shop_list5 = input("Enter fifth item for shopping: \n").title()
shop_list.append(shop_list4)
shop_list.append(shop_list5)

# converting back to tuple 
new_shop_list = tuple(shop_list)

# output
print("|".join(new_shop_list))

# 6

