
item_list = ["Rice", "Beans", "Yam", "Semo", "Garri"]
price = [2500, 2000, 3000, 1500, 1200]
supermart = {
    "Items": item_list,
    "Price": price
}
print("You are welcome to Pace Supermarket.")
print("Check our available goods and price, then order per quantity")
print("\n")
print("--" * 16)
print("Available goods and there price")
print("--" * 16)
for itemm, pricee in zip(supermart["Items"], supermart["Price"]):
    print(f"{itemm:<10} {pricee:>10}")
print("--" * 16)
print("Enter your negotiated price below ")
user_price_1 = input("Enter your price for Rrice: \n"))
user_price_2 = input("Enter your price for Beans: \n"))
user_price_3 = input("Enter your price for Yam: \n"))
user_price_4 = input("Enter your price for Semo: \n"))
user_price_5 = input("Enter your price for Garri: \n"))
user_price = [user_price_1, user_price_2, user_price_3, user_price_4, user_price_5]
supermart.update({"Price": user_price})
print(supermart)