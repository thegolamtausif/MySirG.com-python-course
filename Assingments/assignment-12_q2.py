#first N natural numbers
a=5
print("first %d natural numbers in reversed order are - "%a,end=" ")
def nn(n):
    if n>0:
      print(n,end=",")
      nn(n-1)
    else:
       return 0
nn(a)