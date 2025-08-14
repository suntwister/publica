
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