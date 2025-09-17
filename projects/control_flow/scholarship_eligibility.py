# Government Scholarship ELigibility
print(" Federal Government Scholarship Eligibility Checker \n")

# general questions
citizen = input("Are you a citizen of Nigeria? (yes/no): ").lower()
enroll = input("Are you a full-time undergraduate in a Nigerian university? (yes/no): ").lower()
other_scholarship = input("Are you currently on another Oil & Gas scholarship? (yes/no): ").lower()

# Academic qualification
print("\n Enter your 5 WAEC subjects and their grades (A, B, C, D, E, F)")
academic = {}
for i in range(5):
    subject = input(f"Enter subject {i+1}: ").title()
    grade = input(f"Enter the grade for {subject}: ").upper()
    academic[subject] = grade

# conditions 
eligibility = True

if citizen != "yes":
    eligibility = False
elif enroll != "yes":
    eligibility = False
elif other_scholarship == "yes":
    eligibility = False

# verifying o'level result
for key,value in academic.items():
    if value not in ["A", "B"]:
        eligibility = False
        break

# scholarship result output

print("---RESULT---")
if eligibility:
    print("Congratulations, you are eligible for the goverment scholarship")
else:
    print("Sorry, you are not eligible for the scholarship")