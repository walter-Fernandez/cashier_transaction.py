#Explanation of the program
#this program is a cashier system
#program allow you to input upper or lowercase BALANCE, WITHDRAW or DEPOSIT
#Your balance is $1000
# if you input DEPOSIT or WITHDRAW
#then input the amount as a integer with no string
#and the program is going to add or take out that amount from the balance
#NOTE: this program does not accept float data type
balance = "$"+str(1000)
int_balance = 1000
def bank():
    global balance
    global int_balance
    cashier = input("How can I help you today?\n BALANCE\tWITHDRAW\tDEPOSIT\t:")
    #while question == "yes" or "YES":
    while cashier =="BALANCE" or cashier == "BALANCE".lower() or cashier == "WITHDRAW" or cashier == "withdraw".lower() or cashier == "DEPOSIT" or cashier == "DEPOSIT".lower():
       if cashier =="BALANCE" or cashier == "BALANCE".lower():

               print("your balance is: "+ balance)
               break
       elif cashier == "WITHDRAW" or cashier == "withdraw".lower():
           cashier = input("write the amount you would like to withdraw: ")
           while not cashier.isdigit():  # the word contains only digits
               cashier = input("WRONG INPUT, please enter an integer")

           else :
               print("$",int(int_balance) - int(cashier))
       elif cashier == "DEPOSIT" or cashier == "DEPOSIT".lower():
           cashier = input("please, input the amount you would you like to deposit:  ")
           print( int(int_balance)+int(cashier))
           while not cashier.isdigit():
                   cashier = input("WRONG INPUT, please enter an integer ")
              #new_balance = int(int_balance) + int(cashier)
              #print(new_balance)
       else:
           cashier = input("How can I help you today?\n BALANCE\tWITHDRAW\tDEPOSIT\t:")

bank()