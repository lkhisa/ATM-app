#register -first name, last name, password, email  generate user account
#login -account number, password
#bank operations
#Initializing the system

import random
database={}  #dictionary
def init():

    print("Welcome to bankPHP")

    haveAccount=int(input("Do you have an account with us?: 1 (yes) 2 (no) \n"))
    if(haveAccount==1):
        login()
    elif(haveAccount==2):
        register()
    else:
        print("You have selected invalid option")        
        init()
    


def login():
    print("********LOGIN********")

    accountNumberFromUser=int(input("What is your account number? \n"))
    password=input("What is your password? \n")

    for accountNumber, userDetails in database.items():
        if(accountNumber==accountNumberFromUser):
            if(userDetails[3]==password):
                bankOperation(userDetails)

    print('Invalid account or password')
    login()            


def register():
      print("******REGISTER*****")     
      email=input("What is your email address \n")
      first_name=input("What is your first name \n")
      last_name=input("What is your last name \n")
      password=input("Create your password \n")

      accountNumber=generateAccountNumber()

      database[accountNumber]=[first_name, last_name, email, password]

      #return database
      import datetime
      e=datetime.datetime.now()
      print("Your account has been created")
      print("=== ==== ===== ===== ===== ==")
      print("Your account number is: %d" % accountNumber)
      print("Make sure to keep it safe")
      print("== ==== ===== ===== ==== ==== =")
      print('date and time =%s' % e)

      login()

def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1] ))

    isSelectedOptionValid=False
    while isSelectedOptionValid==False:
        selectedOption=int(input("What would you like to do?: 1 (deposit) 2 (withdraw) 3 (complain) 4 (exit) \n"))

        if(selectedOption==1):
           
            depositOperation()
        elif(selectedOption==2):
            
            withdrawalOperation()
        elif(selectedOption==3):
              
            complain()
        elif(selectedOption==4):
            
            exit()        
        else:
            print("Invalid option selected")
            bankOperation(user)    

def withdrawalOperation():
    print("How much would you like to withdraw?")

    amount=int(input('Write amount \n'))
    print('Take your cash')
def depositOperation():
    print("How much would you like to deposit?")

    amount=int(input('Write amount \n'))
    print('Thank you for banking with us.')

def complain():
    print('What issue would you like to report?')
    issue=input('Report any issues here \n')
    print('Thank you for contacting us.')


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

   ###Actual banking system
init() 
#print(generateAccountNumber())