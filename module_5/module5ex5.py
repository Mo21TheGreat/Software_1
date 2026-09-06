attempts = 0

while attempts < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "python" and password == "rules":
        print("Welcome")
        break
    
    attempts += 1
    
    if attempts == 5:
        print("Access denied")
    
    else:
        print("Incorrect username or password. Please try again.")
    