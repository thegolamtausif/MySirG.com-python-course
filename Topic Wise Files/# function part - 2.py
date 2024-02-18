# function part - 2
def add():
    #takes nothing returns nothing
    a=int(input("enter  first number - "))
    b=int(input("enter  second number - "))
    c=a+b
    print("sum is - ",c)
add()

#takes ssomething return nothing
def add(a,b):
   c=a+b
   print("sum is - ",c)
add(10,29)


#takes nothing return something 
def add():
   a=int(input())
   b=int(input())
   c=a+b
   return(c)
x=add()
print(x)

#takes something return something 
def add(a,b):
   c=a+b
   return(c)
x=add(10,20)
print(x)
