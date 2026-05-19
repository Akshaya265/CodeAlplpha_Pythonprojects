AAPL = 180
TSLA = 250

stock = input("Enter stock: ")
qty = int(input("Quantity: "))

if stock == "AAPL":
    total = AAPL * qty
elif stock == "TSLA":
    total = TSLA * qty

print("Total investment:", total)
    