# Task 1
input_1 = str(input("Enter your favourite quote: "))
# converting input
conv_input = input_1.title()
print("\"" + conv_input + "\"")

# Task 2
Emp_list = []
shop_1 = input("Enter shopping item 1: ")
shop_2 = input("Enter shopping item 2: ")
shop_3 = input("Enter shopping item 1: ")
Emp_list.append(shop_1)
Emp_list.append(shop_2)
Emp_list.append(shop_3)
New_list= list(Emp_list[0] +  Emp_list[1] + Emp_list[2])
print(New_list)

# Task 3
input_2 = str(input("Kindly enter a sentence:\n"))
split_input = list(input_2)
print(len(split_input))

# Task 4
input_3 = input("Pls enter 5 of your names seperated by space:\n ").split()
input_3 = [input_3.lower() for input_3 in input_3]
sort1 = sorted(input_3)
print("\n".join(sort1))

# Task 5
name_list = []
score_list = []
input_name_1 = input("Pls enter your first student name:\n ")
input_name_2 = input("Pls enter your second student name:\n ")
input_name_3 = input("Pls enter your third student name:\n ")
name_list.append(input_name_1)
name_list.append(input_name_2)
name_list.append(input_name_3)
print(name_list)
input_score_1 = input(f"Enter the score for {input_name_1}\n: ")
input_score_2 = input(f"Enter the score for' {input_name_2}\n: ")
input_score_3 = input(f"Enter the score for' {input_name_3}\n:" )
score_list.append(input_score_1)
score_list.append(input_score_2)
score_list.append(input_score_3)
print(score_list)
print(f"{name_list[0]}:\t{score_list[0]} \n{name_list[1]}:\t{score_list[1]} \n{name_list[2]}:\t{score_list[2]}")

# Task 6
input_word = input("Enter a word: ")
print(len(input_word))
check_upper = input_word.isupper()
check_lower = input_word.islower()
check_title = input_word.istitle()
revers = input_word[::-1]
print(revers)

# Task 7
cities = ["Lagos", "Ibadan", "Abeokuta", "Ijebu-ode", "Shagam"]
#print(cities)
cities[2] = "Ilorin"
cities.insert(0, "Abuja")
print(cities[0:4])