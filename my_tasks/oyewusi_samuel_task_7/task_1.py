# collecting user bio-data
user_name = input("Enter your full name: ")
user_age = input("Enter your age: ")
user_gender = input("Enter your gender: ")
user_course = input("Enter 4 courses seperated by space: ").title().split()

# bio-data in dictionary
user_bio_data = {
    "Name": user_name.title(),
    "Age": user_age,
    "Gender": user_gender.title(),
    "Course": user_course
}
print("--------------------------------------------------------")
print("Your student bio-data")
print("--------------------------------------------------------")
print(f" Name: \t\t|\t {user_bio_data['Name']}\n Age: \t\t|\t {user_bio_data['Age']}\n Gender \t|\t {user_bio_data['Gender']}\n course: \t|\t {", ".join(user_bio_data['Course'])}")
print("--------------------------------------------------------")
