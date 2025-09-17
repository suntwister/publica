import csv
from pathlib import Path
from participant_pkg.file_ops import save_participant, load_participants

# CSV file path
file_path = "participant_pkg/contacts.csv"

# collecting perticipant details

while True:
    
    name = input("Enter participant name: ")
    if not name.isalpha():
        print("Invalid input: Participant name cannot be a number please try again.")
        continue
    try:``
        age = int(input("Enter participant age: "))
        if age <= 0:
            print("Age must be a positive integer.")
            continue
    except ValueError:
        print("Age must be a number")
        continue
        
    phone = input("Enter participant phone: ")
    if not phone.isdigit():
        print("Phone must be a number")
        continue
    if len(phone) != 11:
        print("Phone number should not exceed 11 characters.")
        continue
    if phone 
    
    track = input("Enter participant track: ")
    if not track:
        print("track cannot be empty")
        continue

    # saving participant data into dictionary
    participant_dict = {
        "Name": name,
        "Age": age,
        "Phone": phone,
        "Track": track
    }
    
    save_participant(file_path, participant_dict)

    # If everything passed
    print("\nParticipant registered successfully!")

    # to add another participant
    another_participant = input("will you like to add another participant: (y/n): ")
    if another_participant != "y":
        break

    break

load_participants(file_path)