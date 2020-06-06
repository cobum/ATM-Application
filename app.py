from datetime import datetime
import getpass
import querydb as query
import re
import smtplib
from email.mime.text import MIMEText





def display_dashboard():

     #username,password=atmLogin()
     account_number,balance,fullname,email = query.query_db(query.customer_info_query,'kaka','kaka')[0]
     print("**"*15, "Welcome to CAS BANK" ,"**"*20)
     print ('*',' '*87 ,'*')
     print ('*',' '*87 ,'*')
     print("**"*15,datetime.now(). strftime("%Y-%m-%d %H:%M"),"**"*21)
     print ('*',' '*87 ,'*')
     print ('*'*5,'Customername: {}'.format(fullname),'*'*58 )
     print ('*',' '*87 ,'*')
     print ('*',' '*87 ,'*')
     print ('*'*5,'Acccount Number: {}'.format(account_number),'*'*15,'Balance: {}'.format(balance),'*'*30 )
     print ('*',' '*87 ,'*')
     print ('*',' '*87 ,'*')
     print ('*',' '*87 ,'*')
     print ('*',' '*87 ,'*')
     print("*"*22,"Choose the below options for your Transcations","*"*21)
     print ('*',' '*87 ,'*')
     print ("*"*5,"Check Balance:1","**"*20,"Withdraw:2","*"*15)
     print ('*',' '*87 ,'*')
     print ('*',' '*87 ,'*')
     print ('*',' '*87 ,'*')
     print ("*"*11,"Tranfer:3","**"*20,"Cash Deposit:4","*"*13)
     print ('*',' '*87 ,'*')
     print ('*',' '*87 ,'*')
     print("*"*39,"THANK YOU {}","*"*30)
     print ('*',' '*87 ,'*')
     print ("*"*90)
  

def Check_bal():
    account_number,balance,fullname,email = query.query_db(query.customer_info_query,'kaka','kaka')[0]
    new_balance = query.query_db(query.balance_query,account_number)
    print  ("Your Balance is ${}".format(new_balance))

def Cash_DepositDeposit():
   account_number,balance,fullname,email = query.query_db(query.customer_info_query,'kaka','kaka')[0]
   amount=input("Enter amount to deposit: ")
   query.query_db (query.transfer_to_query,amount,account_number)
   account_number,balance,fullname,email = query.query_db(query.customer_info_query,'kaka','kaka')[0]
   print ("Your account has been credited with $ {}  and your new balance is $ {}".format(amount,balance))


def Cash_withdrawal():
   account_number,balance,fullname,email = query.query_db(query.customer_info_query,'kaka','kaka')[0]
   amount=input("Enter amount to Withdraw: ")
   if amount > balance:
       query.query_db (query.transfer_from_query,amount,account_number)
       account_number,balance,fullname,email = query.query_db(query.customer_info_query,'kaka','kaka')[0]
       print ("Your account has been debited with $ {}  and your new balance is $ {}".format(amount,balance))
   else:
      print("Insufficient  Balance")

def  Cash_Transfer():
   account_number,balance,fullname,email = query.query_db(query.customer_info_query,'kaka','kaka')[0]
   amount=input("Enter Transfer Amount: ")
   receving_account=  input ("Enter Receiving account: ")
   receiver_name = query.query_db (query.receiver_name_query,receving_account)
   if amount < balance:
      query.query_db (query.transfer_to_query,amount,receving_account)
      query.query_db (query.transfer_from_query,amount,account_number)
      account_number,balance,fullname,email = query.query_db(query.customer_info_query,'kaka','kaka')[0]
      print ("You have successfullly transfered ${} to {} and your new balance is ${}".format(amount,receiver_name,balance))
   else:
       print("Insufficient  Balance")
#insert_cusomer_data_query = ("INSERT INTO atm.customer (fullname, username, password, gender, email, date_of_birth) VALUES (%s, %s, %s, %s, %s, %s)")

def CreateNewAccount():
  gender_check_count = 3
  while True:
       fullname = input("Enter FullName: ")
       username = input ("Enter username: ")
       password = getpass.getpass("Enter password : ")
   
       
       gender = input("Enter M or F: ")
       if gender not in ["M","F"]:
          while True:
             gender_check_count-=1
             print ("You must enter M or F")
             gender = input("Enter M or F: ")
             if gender_check_count <=  1:
                 print("Try again later!!!")
                 return False 
       elif gender in ["M","F"]:
            print (gender)
            pass
         
          #return gender
            #continue

       email = input("Enter your email: ")
       date_of_birth = input("Enter of bith: YYYY-MM--DD: ")
       account_type = input("Enter Savings or Current: ")
       opening_amount= int(input("Enter Initial opening amount: "))
       query.query_db(query.insert_cusomer_data_query,fullname, username, password, gender, email, date_of_birth)
       query.query_db(query.insert_account_type ,account_type,opening_amount)
       print ("Your account is all set. Check Your email: ")
       print ("Thank You Banking with US!!!")
       # SendEmail()
       exit(1)


def login(username,password):
  attempts = 3
  print ("Welcome to the login Page")
  #username = input("Enter username : ")
  #password = getpass.getpass("Enter password : ")
  while True:
    if username == username and password== password:
      print("You have successfullly logged in")
      print()
      #return username
      display_dashboard()
      txnTypes()
      return True
    else:
      attempts-=1
      print("You entered incorrect login details")
      print("You have {} attempt".format(attempts) )
      username = input("Enter username again : ")
      password = getpass.getpass("Enter password again  : ")
  
    if attempts <= 1:
      print("Account has been locked!!!")

      return False

  

def atmLogin():
   login_attempt = 3
   print("**"*15, "Welcome to CAS BANK" ,"**"*20)
   print ('*',' '*87 ,'*')
   print ('*',' '*87 ,'*')
   print("**"*15,datetime.now(). strftime("%Y-%m-%d %H:%M"),"**"*21)
   print ('*',' '*87 ,'*')

   try:
     user_input= int(input("Enter 1 to login or 2 to open New Account: "))
   except ValueError:
    print("Value must be a digit")
   user_input = 0
   while True:
    user_input= int(input("Enter 1 to login or 2 to open New Account: "))
    if user_input not in [1,2]:
     login_attempt-=1
     
     print("You have {} more attempt".format(login_attempt))
     user_input= int(input("Enter 1 to login or 2 to open New Account: "))
     if login_attempt <= 1:
       print("You have been locked out. Contact customers service")
       return False
    elif user_input == 1:
       username=input ("Enter username: ")
       password = getpass.getpass("Enter password : ")
       #valid_username,validpass = query.query_db(query.query_login)
       #if username == valid_username and password == validpass:
       if login(username,password):

          login(username,password)
         #how do i use the username and password as paramters in the display_dashboard

    #return username,password
    elif user_input == 2:
       CreateNewAccount()

      
       #break
  # else:
   #open account
  # else:
   #open account

def txnTypes():
  if login:
    #while True:
     txntype = int(input ("Enter transaction type: "))
     if txntype == 1:
       Check_bal()
       #break
     elif txntype == 2:
       Cash_withdrawal()
       #break
     elif txntype ==3 :
       Cash_Transfer()
       #break
     elif txntype == 4:
       Cash_Deposit()
       #break
     else :
       print("I will work on you later")

# def SendEmail():
#    pass
#    account_number,balance,fullname,email = query.query_db(query.customer_info_query,'kaka','kaka')[0]
   
#    fromx = 'mrcastech@gmail.com'
#    to =email
#    Subject = "Your New Account Number "
#    message = "Dear {}. Your New Account Number is {} ".format(fullname,account_number)
#    msg = MIMEText ()
#    msg ['Subject'] = Subject
#    msg ['From'] = fromx
#    msg['To'] = to
#    msg.attach(MIMEText(message,'plain'))
#    server = smtplib.SMTP('smtp.gmail.com:587')
#    server.starttls()
#    server.ehlo()
#    server.login ('mrcastech@gmail.com','Python@123')
#    server.sendmail
#    server.quit()


def main():
  atmLogin()



main()

