def sum(n):
    if n>0:
        ans= n + sum(n-1)
    else:
        return 0
    return ans
x=sum(9)
print(x)
