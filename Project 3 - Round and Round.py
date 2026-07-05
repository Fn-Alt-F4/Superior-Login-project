

#Project 3 - "Round and Round." Wrap the whole thing in a loop so it doesn't just do one action and quit. After logging in or creating an account
#it dumps you back to the menu. Add a "quit" option to break out. New concept: the menu loop, a central hub you keep returning
#to. This is what makes it feel like a real app instead of a script that runs once.



account = {}

while True:
    login_question = input(" Are you logging in or creating an account. either type: 'create' or 'login' ")
    if login_question == "create":
        username = input("whats your username?")
        password = input("Whats your password?")
        account[username] = password
        
    elif login_question == "quit":
        break
    
    elif login_question == "login":
        login_username = input("Whats your username?")
        login_password = input("Whats your password?")
        if login_username in account and account[login_username] == login_password:
            print("Correct login")    
        else:
            print("incorrect login.")
    
    
