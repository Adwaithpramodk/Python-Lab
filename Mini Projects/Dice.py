import random

while True:
    print("----Dice Rolling Simulator----")
    print("1.Roll Dice")
    print("2.Exit")

    user = input("Enter the choice :").strip()

    if user == '1':
        num = random.randint(1,6)
        print(f"The Number is {num}")

    elif user == '2':
        print("Thank you for playing")
        break

    else:
        print("Invalid Choice")