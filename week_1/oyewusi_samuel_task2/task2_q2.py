price = str(input("what is the current price of gari per paint in naira: "))
price_float = float(price)
# convert price to naira and kobo
naira = int(price_float)
kobo = round(price_float - naira * 100)
print(f'The current price of gari per paint is {naira} naira {kobo} kobo')
