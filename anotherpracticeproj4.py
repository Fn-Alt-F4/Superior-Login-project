

accounts = {}

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

while True:
    login_question = input("are you logging in or creating a account. type either 'login' or 'create' ,")
    if login_question == "create":
        create_account()
    elif login_question == "login":
        login_account()
    elif login_question == "quit":
        break
    else:
        print("not an option")