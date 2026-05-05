
class Account:
    def __init__(self ,balance = 0):
        self._balance = balance

    def _is_valid_amount(self,amount):
        return amount > 0

    def deposit (self,amount):
        if self._is_valid_amount(amount):
            self._balance += amount 
            print(f"Amount deposited Successsfully , current balance {self._balance}")
        else:
            print("Amount must be greater than zero")
        
    def withdraw(self,amount):
        if self._is_valid_amount(amount):
            if amount <= self._balance:
                self._balance -= amount
                print(f"Amount Withdrawed Successsfully , current balance {self._balance}")
            else:
                print("Insufficient Funds!")
        else:
            print("Amount must be greater than zero")
    @property
    def balance(self):
        return self._balance
    
ac = None
print("---Welcome To AK Bank---")
while True:
    print("--MENU--")
    print("1.Account Creation")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Balance Checking")
    print("5.Exit")

    n = input('Enter the choice(1/2/3/4/5): ')

    if n == '1':
        ac = Account()
        print(f"Account created at balance {ac.balance}")

    elif n == '2':
        if ac is None:
            print("Create a Account First")
            continue
        try:
            amt = float(input("Enter the amount to deposit: "))
            ac.deposit(amt)
        except ValueError:
            print("Must Enter a Number")

    elif n == '3':
        if ac is None:
            print("Create a Account First")
            continue
        try:
            amt = float(input("Enter the amount to Withdraw: "))
            ac.withdraw(amt)
        except ValueError:
            print("Must Enter a Number")
    
    elif n == '4':
        if ac is None:
            print("Create a Account First")
            continue
        print("Checking Balance ....")
        print(f"Current Balance {ac.balance}")

    elif n == '5':
        print("Closing....")
        break
    

 

        