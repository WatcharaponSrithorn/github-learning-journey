username = input("Enter your username : ")
password = input("Enter your password : ")

if username == "admin" and password == "admin":
    print("Log in sucessful")
elif username == "admin" and password != "admin":
    print("password incorrect")
elif username != "admin" and password == "admin":
    print("username incorrect")
else:
    print("username & password incorrect")