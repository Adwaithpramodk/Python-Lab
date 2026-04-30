st = input("Enter the String :").lower()

space = st.replace(" ","")

txt = space[::-1]

if space == txt :
    print("True")
else :
    print("False")