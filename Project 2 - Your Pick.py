

#Project 2 - "Your Pick." Add a menu at the start: "do you want to log in or create an account?" Based on their answer, branch into
#one path or the other. Creating an account means asking for a username and password and adding them to the dictionary
#New concept: branching into different modes based on user choice, and letting
#the user add to your dictionary at runtime instead of you hardcoding it. This is the "reactive" part you wanted.


#First step, create the menu.

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#accounts = {}

#login_question = input("Type 'login' to login or type 'create' to create an account.")

#while True:
    #if login_question == "create":
        #typed_email = input("Whats your email?")
        #typed_username = input("Whats your username?")
        #typed_password = input("Whats your password?")

        #account1 = typed_email and typed_password and typed_username

        #if account1 == typed_username and typed_password and typed_email:
            #print("correct")
            #break
        #else:
            #print("incorrect.")

#while True:
    #if login_question == "login":
        #loginQ1 = input("Whats your username?")
        #loginQ2 = input("Whats your password?")

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#Honestly I'm lost so here is where the debugged version comes in..

###

###

###

#So the problem I was running into up top was, I was trying to create an if statement instead od actually creating and saving the login for later.
#** I jump ahead to much and dont think about what im typing and why it does it, I get lost. TAKE YOUR TIME....

accounts = {} 

login_question = input("Type 'login' to login or type 'create' to create an account.")
#This is to find out if the user is logging in or creating an account, thats it. 

while True: #We need to create a loop and keep it looping until what comes out is true.
    if login_question == "create":  #We are creating an 'if' statement stating that IF the user chose create, we continue down.
        typed_username = input("Whats your username?")  #We ask the user for their username and save it to typed user.
        typed_password = input("Whats your password?")  #We ask the user for their password and save it to typed password.
        accounts[typed_username] = typed_password       #Now for this, we are saving the typed username as a key in the accounts dictionary and it equals typed password because thats the value from the key.
        print("Account Created!")       #ACCOUNT CREATED
        break           #Break the loop


while True:     #We need to create a if true loop that will loop the login process until the login is TRUE
    if login_question == "login":   #This is if our login question was login from the users input then we contine with the following loop
        login_username = input("Whats your username?")  #Asking what the users username is and storing it in login username
        login_password = input("Whats your password?")  #Asking what the users password is and storing it in login password
        if login_username in accounts and accounts[login_username] == login_password:   #creating our if username is in dictionary and if the key is holding the right value (password) then let us in
            print("Correct login")
            break
        else:
            print("Incorrect login.")
            break


###

###

###

#Even more debugged version


login_question = input("Type 'login' to login or type 'create' to create an account.")

while True:
    if login_question == "create":
        typed_username = input("Whats your username? ")
        typed_password = input("Whats your password? ")
        accounts[typed_username] = typed_password
        print("Account created!")
        break
    elif login_question == "login":
        login_username = input("Whats your username? ")
        login_password = input("Whats your password? ")
        if login_username in accounts and accounts[login_username] == login_password:
            print("Correct login")
            break
        else:
            print("Incorrect login.")
            break
    else:
        print("Type login or create")
        break
