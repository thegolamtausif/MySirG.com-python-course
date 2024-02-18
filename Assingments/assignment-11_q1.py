print(" calculatr lcm of two numbers ")
def lcm(a,b):
    if a>b:
        big=a
    else:
        big=b
    for i in range( big,100000):
        if i%a==0 and i%b==0:
            return i
            break
ans=lcm(10,22)
print("lcm is -",ans)
    
