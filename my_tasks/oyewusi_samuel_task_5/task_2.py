2
# Collecting user best friends names
friend_input = input("Enter your best five friends seperated by space: \n").split()

# converting friends name input to tuple
friend = tuple(friend_input)
print("----------------------")
# output of turple in reverse order
print(friend[::-1])