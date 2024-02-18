#Nth term of fibbonachhi series
def ntof(n):
    f=0
    p=1
    c=0
    while n>0:
          f = p + c 
          p=c
          c=f
          n=n-1
    return f
a=6
ans=ntof(a)
print("%dth term of fibbonachhi series is - %d"%(a,ans))