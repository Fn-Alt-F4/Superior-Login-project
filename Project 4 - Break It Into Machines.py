

#Project 4 - "Break It Into Machines." Now refactor. Take projects 1 through 3 and carve them into functions: a create_account() function, a login() function, a show_menu() function.
#The bottom of your file becomes a clean loop that just calls these. The behavior doesn't change, but the organization does. New concept: decomposition, turning a working-but-messy script into clean named functions.
#This is the single biggest "intermediate" skill and the one you've been building toward.

accounts = {}


login_question = input("are you logging in or creating a account. type either 'login' or 'create' ,")

def create_account():
    create_username = input("Username you want?")
    create_password = input("Password you want?")
    accounts[create_username] = create_password
    print("You have created your account!")

def login_account():
    user_login = input("Whats your username?")
    user_password = input("Whats your password?")
    if user_login in accounts and accounts[user_login] == user_password:
        print("Login sucsessful!")
    else:
        print("Not a real login")

def quit():
    if login_question == "quit":
        break

