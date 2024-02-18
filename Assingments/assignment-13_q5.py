#first N natural numbers
a=6
print("Sum of the   first %d even natural numbers is - "%a,end=" ")
def nn(n):
    if n>0:
      if n%2 == 0  :
         return  n**2 + nn(n-1)
      else:
         return nn(n-1)
    else:
       return 0
x=nn(a*2)
print(x)