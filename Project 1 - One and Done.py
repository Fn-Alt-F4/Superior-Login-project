

#Project 1 - "One and Done." Create a single hardcoded account (username and password stored in a dictionary), then immediately log the user in against it. No choices, no menu. Just: here's an account, now prove
#you can check a login against stored data. New concept: storing credentials in a dictionary and checking input against them, instead of 
#comparing against two loose variables like you've done before. This is the atom everything else is built from.

username = "edogg"

password = "dogee"

stored_login_credentials = {username : password}

while True:
    typed_user = input("Whats your username?")
    typed_password = input("Whats your password?)")
    if typed_user and typed_password == stored_login_credentials:
        print("correct login")
        break
    else:
        print("Incorrect login, please try again.")


###

#Debugged

username2 = "johnpork"  #This is our username

password2 = "porkjohn"  #This is our password

stored_login_credentials2 = {username2 : password2}     #This is our dictionary that is storing our login credentials, the username is the key and the password is the value.

while True:     #This is a while true statement so its a loop until your login is true then we break the loop later.
    typed_user2 = input("Whats your username?")     #This is just a variable for user input to type what their login would be and then so I can use it later to check
    typed_password2 = input("Whats your password?")     #Same as above just for password
    if typed_user2 in stored_login_credentials2 and stored_login_credentials2[typed_user2] == typed_password2:  #checking login in dictionary 
        print("Correct login")  #normal if statement
        break
    else:
        print("Incorrect login.")

###
    