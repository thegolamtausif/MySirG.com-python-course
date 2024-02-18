#Fibbonachhi series
def fib(n):
    a,b,c=0,1,0
    while True:
        if c > n:
            return
        yield a
        a,b=b,a+b
        c+=1
N=15
it=fib(N)
for i in range(N):
    print(next(it))
