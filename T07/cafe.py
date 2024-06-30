
#File cafe.py for Practical Task 2 on T07
#Define menu item
menu = ["Milk Tea", "Coffee", "Pasta", "Bun","Pizza"]

#Define Stock with each Item
stock = {"Milk Tea": 25, "Coffee": 25, "Pasta": 20, "Bun": 20, "Pizza": 20}

#Define Price with each Item
price = {"Milk Tea": 5, "Coffee": 4, "Pasta": 10, "Bun": 5, "Pizza": 12}

#Calculate total price value of the stock in each menu item
total_stock = 0
for item in menu:
    item_value = stock[item] * price[item]
    print(f"Sub-total value of {item} is £{item_value}. Stock: {stock[item]}, price: {price[item]}")
    total_stock += item_value

print(f"Total price value of overall stock is £{total_stock}")

