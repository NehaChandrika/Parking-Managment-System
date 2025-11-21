print("Enter 1 to add item into stock")
print("Enter 2 to remove an item")
print("Enter 3 to view stock")
print("Enter 4 to view sales")
print("Enter 5 to view shortage items")
print("Enter 6 to EXIT")

shortage = []
stock = {}
sales = {}

choice = int(input("Enter your choice: "))

while choice != 6:
    if choice == 1:
        item = str(input("Enter the item to add: "))
        quantity = int(input("Enter the quantity: "))
        if item in stock:
            stock[item] = stock[item]+ quantity
        else:
            stock[item] = quantity

    elif choice == 2:
        if len(stock) == 0 :
            print("stock is empty")
            break
        item = str(input("Enter the item to remove/sell: "))
        if item not in stock:
            print("Item not in stock to sell")
        quantity = int(input("Enter the quantity: "))
        if stock[item] < quantity:
            print(f"Sorry, not enough stock to sell ")
        else:
            stock[item] = stock[item] - quantity
            if item in sales:
                sales[item] = sales[item] + quantity
            else:
                sales[item] = quantity

    elif choice == 3:
        print("Current Stock:", stock)

    elif choice == 4:
        print("Sales Record:", sales)

    elif choice == 5:
        shortage = []
        for el in stock:
            if stock[el] < 5:
                shortage.append(el)
        print("Shortage Items:", shortage)

    else:
        print("Enter valid input")

    
    choice = int(input("\nEnter your choice: "))