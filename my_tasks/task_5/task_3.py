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
