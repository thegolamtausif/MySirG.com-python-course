#factorial of a number 
num=4
def fact(num):
    if num>1:
       return num * fact(num-1)
    else:
        return 1
ans=fact(num)
print("factorial of %d is %d"%(num,ans))