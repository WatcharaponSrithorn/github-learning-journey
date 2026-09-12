# innput from user
username = input("Enter your username : ")
password = input("Enter your password : ")

# check condition for login
if username == "admin" and password == "admin": # check if both 2 conditions are true
    print("Log in sucessful")
elif username == "admin" and password != "admin":
    print("password incorrect")
elif username != "admin" and password == "admin":
    print("username incorrect")
else:
    print("username & password incorrect")