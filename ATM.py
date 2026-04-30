print("Welcome to ATM")

ac = 0
while True:
    print("-----MENU-----")
    print("Select the Option From the below")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    user = input("Enter the choice (1/2/3/4) :")
    if user == '1':
        print("Available balance :",ac)
    
    elif user == '2':
        try :
            amt = int(input("Emter the amount :"))
            if amt > 0 :
                ac = ac + amt
                print("Available balance :",ac)
            else :
                print("Amount must be positive")
        except :
            print("Invalid Input")

    elif user == '3':
        try :
            amt = int(input("Enter the amount to withdraw :"))
            if amt <= 0 :
                print("Amount must be positive")
            elif amt > ac :
                print("Insufficient balance")
            else:
                ac = ac - amt
                print("Withdrawal successful")
        except :
            print("Invalid Syntax")
    elif user == '4':
        print(" Thank You")
        break

    else :
        print("Invalid choice")