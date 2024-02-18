def prime(n):
    print("first %d prime numbers are - "%n,end=" ")
    for i in range(1,100000):
        if n>0:          
           for j in range(2,i):             
               if i%j==0:
                  break
           else:
               print(i,end=",")
               n=n-1
prime(10)