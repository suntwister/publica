# declaring list for goods and price
items = ["Book", "Pen", "Pencil", "Eraser", "Bag", "Shoe", "math set", "graph book", "card board" ]
items_price = [500, 100, 100, 50, 2500, 3500, 2000, 150, 200]

# our initioal total before order
cart_total = 0

# taking first 4 items as example for order
cart_total += items_price[0]
cart_total += items_price[1]
cart_total += items_price[2]
cart_total += items_price[3]

# Print items and total
print(f"Items: {items[:4]}")  
print(f"Total Price: ₦{cart_total}")

