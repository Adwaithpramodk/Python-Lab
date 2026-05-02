# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8
# Then, the output should be:
# 40320

def fact(n):
    if n == 0:
        return 1
    else :
        return n*fact(n-1)
    
try:
    n = int(input("Enter the Number :"))
    if n < 0:
        print("Number Must be Greater than Zero")
    else :
        res = fact(n)
        print(res)

except ValueError:

    print("Must Enter a Number")