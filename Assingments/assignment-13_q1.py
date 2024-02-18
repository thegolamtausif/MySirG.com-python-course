#first N natural numbers
a=6
print("Sum of the  first %d natural numbers is - "%a,end=" ")
def nn(n):
    if n>0:
      return  n + nn(n-1)
    else:
       return 0
x=nn(a)
print(x)