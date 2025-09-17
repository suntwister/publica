# Simulated USSD Menu Interaction
print("Welcome to the Naija Mobile service")

# conditioning
code = ""
balance = 5000    
while code != "*123#":
    code = input("Kindly dial code *123# for interaction: ")

print("\nMenu:")
print(" 1: Check Balance\n 2. Buy Airtime\n 3. Buy Data")
choice = input("Enter your choice: ")

# Selection conditions
if choice == "1":
    print("\n You selected: Check Balance")
    print(f"Your airtime balance is ₦{balance} ")
elif choice == "2":
    print("\n You selected: Buy Airtime")
    recharge = int(input("Enter the amount to recharge: "))
    print(f"You have succesfully recharge ₦{recharge}")
    balance -= recharge
    print("Your Account balance is ₦",balance)
elif choice == "3":
    print("\n You selected: Buy Data")
    data_dictionary = {
        "sn": [1,2,3,4,5],
        "data": ["100kb", "500kb", "1gb", "3gb", "5gb"],
        "amount": [200, 600, 1500, 3500, 5500]
    }
    print(f"SN \t Data \t Amount")
    print(f"\n{'SN'}\t{'Data'}\t{'Amount(₦)'}")
    print("-" * 30)
    for i in range(len(data_dictionary["sn"])):
        print(f"{data_dictionary['sn'][i]}\t{data_dictionary['data'][i]}\t₦{data_dictionary['amount'][i]}")
    data_recharge = int(input("Select option from (1 -5): "))
    
    if data_recharge in data_dictionary["sn"]:
        index = data_recharge - 1
        if data_dictionary["amount"][index]>balance:
            print("Insufficient fund, kindly recharge")
        else:
            print(f"\nYou have successfully purchased {data_dictionary['data'][index]} for ₦{data_dictionary['amount'][index]:,}.")
            balance -= data_dictionary["amount"][index]
            print("Your Account balance is ₦",balance)
            print("Thanks for using Naija Mobile Service.")
    else:
        print("Invalid selection! Please try again.")
else:
    print("You have entered an invalid number, please try again")