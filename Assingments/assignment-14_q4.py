class insb(ZeroDivisionError):
    def __init__(self,arg):
        self.msg=arg   
class account:
    rate_of_interrest=7.5 #static variable 
    def __init__(self,a,b):
        self.balance=a
        self.account_number=b
    def show_balance(self):
        print(" $ Current avilable balance is - ",self.balance)
    def show_rate_of_interest(self):
        print("Rate of interest is -",self.rate_of_interrest)
    def withdraw(self):
        amount=int(input("Enter the amount you want to withdraw - "))
        try:
          if amount>self.balance:
              raise insb("Insufficient balnce in bank account.")
          else:
              print("Processing your request....")
              self.balance=self.balance - amount
              print("Done")
        except insb as i:
               print("Process cancelled",i.msg)
        finally:
            self.show_balance()
    def deposite(self):
        amount=int(input("Enter the amount you want to deposite - "))
        print("Processing your request ....")
        self.balance=self.balance + amount
        print("Done.")
        value=input("Enter y to see the current balance - ")
        if value=="y":
            self.show_balance()
        
tausif=account(2500,75166)
tausif.withdraw()
tausif.deposite()
tausif.withdraw() 
tausif.show_rate_of_interest()

