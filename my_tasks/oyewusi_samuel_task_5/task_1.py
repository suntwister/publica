# Collecting user favourite dishes
dish_1 = input("Enter your first favourite nigerian dish: \n")
dish_2 = input("Enter your second favourite nigerian dish: \n")
dish_3 = input("Enter your third favourite nigerian dish: \n")
print("----------------------")
# converting inputs to list
list1 = [dish_1, dish_2, dish_3]

# converting list to tuple
dishes = tuple(list1)

print("\n".join(dishes))