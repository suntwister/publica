# Task 4: Unique Voters Registration System

voters = set()

# First voter
name1 = input("Enter voter name: ")
if name1 in voters:
    print("Warning: This voter is already registered.")
else:
    voters.add(name1)

# Second voter
name2 = input("Enter voter name: ")
if name2 in voters:
    print("Warning: This voter is already registered.")
else:
    voters.add(name2)

# Third voter
name3 = input("Enter voter name: ")
if name3 in voters:
    print("Warning: This voter is already registered.")
else:
    voters.add(name3)

print("Total unique voters:", len(voters))
