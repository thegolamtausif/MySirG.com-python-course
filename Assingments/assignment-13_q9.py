#Nth term of fibbonachhi series
def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
f=1  
x=fib(f-1)
print(x)