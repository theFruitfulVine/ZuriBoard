import datetime

name = input("What is your name? ")
allowedUsers = ['Peter', 'James', 'John', 'Paul']
allowedPasswords = ['passwordPeter', 'passwordJames', 'passwordJohn', 'passwordPaul']

if (name in allowedUsers):
    password = input ("Please input your password: \n")
    userId = allowedUsers.index(name)
    
    if (password == allowedPasswords[userId]):

        print ("\nWelcome %s" %name)
        presently = datetime.datetime.now()
        print ("Current date and time :", presently.strftime("%d:%m:%Y %H:%M:%S \n"))

        print ("These are the available options:")
        print ("1. Cash Withdrawal")
        print ("2. Cash Deposit")
        print ("3. Complaint")

        userSelection = int(input("\nWhat would you like to do? "))

        if (userSelection == 1):
            cashWithdrawn = int(input("How much do you want to withdraw? "))
            print("Take your cash of %d" % cashWithdrawn)
        
        elif (userSelection == 2):
            currentBalance = 0
            deposit = int(input("How much do you want to Deposit? "))
            print("Deposit duccessful! Your current balalnce is", currentBalance + deposit)
        
        elif (userSelection == 3):
            complaint = input("What issue will you like to report? ")
            print ("Thank you for contacting us")
        
        else:
            print ("Invalid selection, please try again")
    
    else:
        print ("Invalid password, please try again")

else:
    print ("Incorrect name, please try again")