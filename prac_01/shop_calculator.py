total_price = 0.00
error_check = True

total_items = int(input("Enter amount of items: "))


while  total_items <= 0:
        print("Invalid number of items")
        total_items = int(input("Enter a valid amount of items: "))

for i in range(1, total_items + 1, 1):
    item_price = float(input("Enter price of item {}:".format(i)))
    total_price = total_price + item_price

if total_price > 100:
    total_price = total_price * 0.9

print("Total price for {} items is ${:.2f}".format(total_items, total_price))
