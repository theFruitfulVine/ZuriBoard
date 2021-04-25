import datetime
import random

customerData = {}

def menu():
    
    print ("Welcome to Heaven's Treasury")
    presently = datetime.datetime.now()
    print ("Current date and time :", presently.strftime("%d:%m:%Y %H:%M:%S \n"))

    invalidSelection = False

    while invalidSelection == False:
    
        acctValidator = int(input("Do you have a Treasury Account? 1 (Yes) 2 (No) \n"))

        if (acctValidator == 1):
            invalidSelection = True
            login()
        elif (acctValidator == 2):
            invalidSelection = True
            print (register())
        else:
            invalidSelection = False
            print ("Invalid selection! Please try again")

def login():
    print("<<< Welcome to the Login Page >>>")

    userAccNo = input("What is your account number? \n")
    password = input("What is your password? \n")

    atmTransactions ()

def register():
    print ("<<< Welcome to Account Creation page. >>>\n")
    fname = input("What is your first name? \n")
    lname = input("What is your last name? \n")
    email =  input("What is your email address? \n")
    password = input("Create your password \n")

    acctNo = createAccNum()
    
    customerData[acctNo] = [fname, lname, email, password]

    print ("Welcome %s. Your account has been created" % (fname +" "+lname))
    print ("Your account number is", acctNo)

    login()

def createAccNum():
    return random.randrange(0000000000,9999999999)

def atmTransactions():

    print ("Login successful")
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

menu()
