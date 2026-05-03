def add(a,b):
    print(f"{a} + {b} = {a+b}")

def sub(a,b):
    print(f"{a} - {b} = {a-b}")

def mul(a,b):
    print(f"{a} x {b} = {a*b}")

def div(a,b):
    if b == 0:
        print("Division By Zero not Possible")
    else:
        print(f"{a} / {b} = {a/b}")

while True:
    print("---Calculator MENU---")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    user = input("Enter the choice(1/2/3/4 ): ")

    if user not in ['1','2','3','4','5']:
        print("Invalid Input")
        continue

    try:
        x , y = map(int,input("Enter two Number: ").split())
        match user:
            case '1':
                add(x,y)
            case '2':
                sub(x,y)
            case '3':
                mul(x,y)
            case '4':
                div(x,y)
            case '5':
                print("Exiting!!")
                break
            case _:
                print("Invalid Choice")
    except ValueError :
        print("Must Enter Numbers")