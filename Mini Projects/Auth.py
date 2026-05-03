db = {
    'arun':'1234',
    'kumar':'0987'
}

# making it as attempt based
for i in range(3):
    print("--Simple Authentication--")

    user = input("Enter Username: ").strip()
    pwd = input("Enter Password: ").strip()

    if user in db and db[user] == pwd:
        print("Login Sucess")

    else:
        print("Login Failed")
