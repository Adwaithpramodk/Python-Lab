import random

level = input("Difficulty (easy/hard) :")

if level == 'easy':
    limit = 50
else :
    limit = 100

num = random.randint(1,limit)
print(num)
attempt = int(input("Enter the number of attempts :"))

i = 1
while i <= attempt :

    guess = int(input("Guess the Number between 1 to 100 :"))

    if guess > num :
        print("Higher")

    elif guess < num :
        print("Lower")

    else:
        print("Congrats the Number is Correct")
        break
    i =i +1
else:
    print(f"Correct Number is {num}")