import random
import datetime
database={1175761664: ['Loretta', 'Khisa', 'lorettakhisa15@gmail.com', 'lolop'], "Balance":200}  
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
    
    is_valid_account_number=account_number_validation(accountNumberFromUser)
    
    if is_valid_account_number:

        password=input("What is your password? \n")

        for accountNumber, userDetails in database.items():
            if accountNumber==int(accountNumberFromUser):
                if(userDetails[3]==password):
                    bankOperation(userDetails)

        print('Invalid account or password')
        login()   
    else:
        init()                   
def account_number_validation(accountNumberFromUser):
    if(accountNumberFromUser):

        if len(str(accountNumberFromUser)) ==10:

            try:
                int(accountNumberFromUser)
                return True
            except ValueError:
                print("Invalid account number, account number should be an integer")
                return False 
            except TypeError:
                print("Invalid account number")
                return False       

        else:
            print("Account number can only be 10 digits")    


    else:
        print('Account number is a required field')    

def register():
      print("******REGISTER*****")     
      email=input("What is your email address \n")
      first_name=input("What is your first name \n")
      last_name=input("What is your last name \n")
      password=input("Create your password \n")

      accountNumber=generateAccountNumber()

      database={accountNumber:[first_name, last_name, email, password], "Balance":0
      }
      
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
    if(database["Balance"]>amount):
        print('Take your cash')
        balance=database["Balance"]-amount
        print("Your balance is %d" % balance)
    else:
        print("you cannot withdraw that amount")

def depositOperation():
    print("How much would you like to deposit?")

    amount=int(input('Write amount \n'))
    balance=database["Balance"]+amount
    print('Your balance is %d' % balance)

def complain():
    print('What issue would you like to report?')
    issue=input('Report any issues here \n')
    print('Thank you for contacting us.')


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

init() 
exit()
