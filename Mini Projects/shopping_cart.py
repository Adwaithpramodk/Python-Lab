cart = {}

print("---Shopping Cart---")

while True:
    print("---MENU---")
    print("1.Add Item")
    print("2.Remove Item")
    print("3.View Cart")
    print("4.Clear Cart")
    print("5.Exit")

    n = input("Enter the choice(1/2/3/4/5)")

    if n == '1':
        item = input("Enter the Item Name: ")
        try:
            cost = float(input("Enter the cost for one item: "))
            q = int(input("Enter the Quantity: "))

            if cost <=0 or q <= 0:
                print("Cost and Quantity must be 1 or above")
                print("Try again !!")
                continue
            if item in cart:
                cart[item]["qty"] += q
                print(f"{item} Quantity updated")
            else:
                cart[item] = {'price':cost,'qty':q}
                print("Item added Successfully")

        except ValueError:
            print("Cost and Quantity Must be Numeric")
            print("Try again !!")
            continue
    elif n == '2':
        rem_item = input("Enter the item to remove: ")

        if rem_item in cart:
            cart.pop(rem_item)
            print("Item Removed successfully")
        else:
            print("Item is not found in cart")
            print("Try again !!")

    elif n == '3':
        if not cart:
            print("Empty Cart")
            continue
        print("Printing item in cart")
        total = 0
        for k,l in cart.items():
            s = l["price"] * l["qty"]
            total += s
            print(f"Item:{k} | price:{l['price']} | Quantity:{l['qty']} | Total: {s}")
        print(f"Total Price:{total}")

    elif n == '4':
        cart.clear()
        print("Cart cleared Successfully")

    elif n == '5':
        print("Closing Cart")
        break

    else:
        print("Invalid Choice , Try again")
        continue


    
    
