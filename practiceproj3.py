

#Project 3 - "Round and Round." Wrap the whole thing in a loop so it doesn't just do one action and quit. After logging in or creating an account
#it dumps you back to the menu. Add a "quit" option to break out. New concept: the menu loop, a central hub you keep returning
#to. This is what makes it feel like a real app instead of a script that runs once.

accounts = {}

while True:

    login_questions = input("Are you logging in or creating an account? type 'login' or 'create'. ")
    if login_questions == "create":
        create_username = input("Whats your username?")
        create_password = input("Whats your password?")
        accounts[create_username] = create_password
    elif login_questions == "login":
        login_username = input("Whats your username?")
        login_password = input("Whats your password?")
        if login_username in accounts and accounts[login_username] == login_password:
            print("Correct login.")
        else:
            print("incorrect login info.")
    elif login_questions == "quit":
        break

##

#line 7 is a while true loop, so we want this login sequence to loop until we are finished with it or until the user quits.
#line 9 is our accounts dictionary, this is where we are going to store all the created usernames and passwords.
#line 11 is our login question. this will help the user decide if they want to login to an account or create one.

# "create" statement
#line 12 is an "if" statement. if the user responded to our login question with create, then we will go down the create loop.
#line 13 is for creating a variable that stores the users typed username
#line 14 is for creating a variable that stores the users typed password
#line 15 is storing that username and password into the dictionary

# "login" statement
#line 16 is else if our login question the user responds with login, it takes them through the login sequence.
#line 17 is for creating a variable that stores the users login username they typed in
#line 18 is for creating a variable that stores the users password they typed in to login to their account
#line 19 is an if statement that asks if the username is in accounts and if accounts username = the stored key (or the stored password, the password is a key)
#line 20 is if the username and password are stored in the accounts dictionary then they login
#line 21 is an else statement
#line 22 is tied to our else statement that goes off if the login was incorrect
#line 23 is an else if statement that is for if the user types in quit in the login question then the loop breaks
#line 24, the loop breaks

#This version is done without assistance of google or ai, this is purely me...