# football match ticket system
print("\tWelcome to Shooting Stars Match Ticket System\n")

seats = {
    "West Stand": {"price": 1000, "seat_no": (list(range(1,15)))},
    "East Stand": {"price": 1500, "seat_no": (list(range(15,28)))},
    "North Shed": {"price": 2500, "seat_no": (list(range(28,43)))},
    "VIP Section": {"price": 5000, "seat_no": (list(range(43,51)))}
}

# Displaying available seats and price
print("\t\t  Seats available")
print("--" * 33)
print(f" Stand\t\t | Price (₦)  \t | Seats")
print("--" * 33)
for key, value in seats.items():
    print(f"{key} \t | {value['price']} \t | {value['seat_no']}")
print("--" * 33)

# collecting user seat number
seat = int(input("Enter a seat number you want to book from (1-50) "))
booked = False
for key, value in seats.items():
    if seat in value["seat_no"]:
        value["seat_no"].remove(seat)
        print(f"You have succesfully reserve seat number {seat} for ₦{value['price']} in the {key}")
        #booked = True
        next = input("will you like to book another seat, Enter (YES or NO): ").upper()
        if next == "YES":
            seat2 = int(input("Enter a seat number you want to book from (1-50) "))
            for key, value in seats.items():
                if seat2 in value["seat_no"]:
                    value["seat_no"].remove(seat2)
                    print(f"You have succesfully reserve seat number {seat2} for ₦{value['price']} in the {key}")
                    booked = True
                    break

if not booked:
    print("The seat number you entered is either booked or invalid")

# displaying remaining seats
print("\nRemaining Seats:")
for key, value in seats.items():
    print(f"{"--"*33}\n{key} \t | {value['price']} \t | {value['seat_no']}")
print("--" * 33)
