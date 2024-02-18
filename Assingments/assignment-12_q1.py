#first N natural numbers
a=5
print("first %d natural numbers are - "%a,end=" ")
def nn(n):
    if n>0:
      nn(n-1)
      print(n,end=",")
    else:
       return 0
nn(a)