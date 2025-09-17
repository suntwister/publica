# User names
names_input = input("Enter three names separated by commas: ").split(",")

# Converting to a set
set_names = set(names_input)

# Create a dictionary
names_dict = {name: len(name) for name in set_names}

# Print the dictionary
print(names_dict)
