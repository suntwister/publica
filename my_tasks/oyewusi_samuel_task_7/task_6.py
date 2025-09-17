# collecting student informations
name = input("Enter your full name: ")
age = input("Enter your age: ")
gender = input("What is your gender: ")

# collecting user scores
subjects = ("Mathematics", "English", "Computer Science")
scores = tuple(float(input(f"Enter your score for {subject}: ")) for subject in subjects)

# guardian information
guardian_name = input("Enter gurdian name: ")
guardian_phone = input("Enter guardian phone number: ")

# hobbies
hobbies = input("Enter at least three of your hobbies - seperate it by comma: ").split(",")
hobbies_set = set(s.strip() for s in hobbies)

# creating dictionary
student_profiles = {
    "Basic Info": {
        "Name": name.title(),
        "Age": age,
        "Gender": gender.capitalize()
    },
    "Academics": {subj: score for subj, score in zip(subjects, scores)},
    "Guardian": {
        "Name": guardian_name.title(),
        "Phone": guardian_phone
    },
    "Hobbies": list(hobbies_set)
}

# Derived Data
student_profile["Academics"]["Average"] = sum(scores) / len(scores)
student_profile["Basic Info"]["Initials"] = "".join([n[0] for n in name.split()])
student_profile["Hobbies Count"] = len(hobbies_set)

