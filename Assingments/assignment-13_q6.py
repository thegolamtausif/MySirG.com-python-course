a=1234
print("Sum of the digits of  %d is - "%a,end=" ")
def nn(n):
    if n>10:
      return  (n % 10) + nn( n//10 )
    else:
       return n
x=nn(a)
print(x)