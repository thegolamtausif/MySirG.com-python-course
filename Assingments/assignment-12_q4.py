#first N natural numbers
a=7
print("first %d even natural numbers in reversed order are - "%a,end=" ")
def nn(n):
    if n>0: 
       if n%2 ==0:
        print(n,end=",") 
       nn(n-1)
    else:
       return 0
nn(a*2)