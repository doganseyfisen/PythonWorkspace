print(
"""-----------
SIGN IN
-----------
""")
userName = "Rick"
userPass = "121212"
accessRight = 3
while True:
    userNameInp = input("\nEnter your username: ")
    userPassInp = input("Enter your password: ")
    if(userNameInp == userName and
            userPassInp == userPass):
        print("\nLogging in...")
        print("Welcome.")
        break
    elif(userNameInp == userName and
            userPassInp != userPass):
        accessRight -= 1
        print("Your password is wrong.")
    elif(userNameInp != userName):
        accessRight -= 1
        print("Your name is wrong.")
    if (accessRight == 0):
        print("\nYou're account is suspended.")
        break
