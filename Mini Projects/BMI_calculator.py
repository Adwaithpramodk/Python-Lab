print("---BMI Calculator---")

try:
    h = float(input("Enter the Height: "))
    w = float(input("Enter the Weight: "))

    if (h <= 0) or (w<=0):
        print("Values Must be greater than zero")
    else :
        hm = h/100
        hi = hm * hm
        bmi = w/hi
        print(f"BMI Score {bmi:.2f}")
        if bmi  < 18.5:
            print("Under weight")
        elif bmi <  25:
            print("Normal")
        elif bmi >= 25 and bmi <=29.9:
            print("Over Weight")
        else:
            print("Obese")

except ValueError:

    print("values must be Numbers")