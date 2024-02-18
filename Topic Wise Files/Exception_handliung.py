class insufficient_balance(ZeroDivisionError):
    def __init__(self,arg):
        self.msg=arg
balance=5000
amo=int(input("Enter the amount you want to withdraw - "))
try:
     if amo>balance:
         raise insufficient_balance("insufficient balance in bank account.")
     print("wait, processing your request.")
     balance=balance-amo
except insufficient_balance as i:
    print("Process cancelled",i.msg)
finally:
    print("current balance is ",balance)
    