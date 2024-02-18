#first N natural numbers
a=7
print("first %d odd natural numbers  are - "%a,end=" ")
def nn(n):
    if n>0: 
       nn(n-1)
       if n%2 == 1:
        print(n,end=",") 
      
    else:
       return 0
nn(a*2)