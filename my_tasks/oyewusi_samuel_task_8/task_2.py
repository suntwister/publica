
"""name = input("Enter your name: ") # collect the user name
age = int(input("Enter your age: ")) # collect the user age which must be an integer
score = int(input("Enter your test score: ")) # collect the user score also must be an integer

eligibility = (age < 18) and (score > 70) # checks if the input age is less than 18 and the score is above 70, it assign a boolean true to the variable if both conditions are true, else false
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")"""

# Scholarship eligibility requirement 
print("Federal Government Scholarship Eligibility Checker")
user_name = input("Enter your full name: ").capitalize()
user_citizen = input("Are you a citizen of nigeria (Enter YES or NO): ").capitalize()
user_inst = input("Are you a registered, full-time undergraduate student in a recognized Nigerian university. (Enter YES or NO): ").capitalize()
user_schlp = input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international. (Enter YES or NO): ").capitalize()
user_aca = input("Did you have five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics. (Enter YES or NO): ").capitalize()

eligibility = (user_citizen == "Yes") and (user_inst == "Yes") and (user_schlp == "No") and (user_aca == "Yes")
result = {True: "you are eligible for the scholarship", False: "you are not eligible for the scholarship"}
print("--" * 20)
print(f"{user_name}: {result[eligibility]}")
print("--" * 20)
