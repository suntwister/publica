# Store Inventory
print("\t Welcome to Oluwatobi Book Store\n")

# Initial store 
store = {
    "Notebook": 80,
    "Pen": 77,
    "Pencil": 60,
    "Eraser": 65,
    "Ruler": 20,
    "Marker": 15,
    "Highlighter": 6,
    "Textbook": 12,
    "Bag": 8,
    "Sharpener": 42,
    "Calculator": 10,
    "Drawing Book": 16
}

store_c = store.copy()

# collecting user cart
cart = {}
print("These are our available items")
print(store)
cart_in = input("Kindly enter all the items you want to get seperated by coma: ").title().split(",")
cart_in = [item.strip() for item in cart_in]
for i in range(len(cart_in)):
    item = cart_in[i]
    quantity = int(input(f"How many quantities of {item}: "))
    cart[item] = quantity

for key, value in cart.items():
    if key in store:
        if value <= store[key]:
            store[key] -= value
            print(f"{value} {key}(s) added to your cart")
        else:
            print(f"Not enough stock for {key}, only {store[key]} left")
    else:
        print(f"Item '{key}' not found in store")

print(f"Before purchase: {store_c}")
print("--" * 10)
print(f"After purchase: {store}")