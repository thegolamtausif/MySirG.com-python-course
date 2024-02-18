
def avg(*n):
    s=0
    noe=len(n)
    for i in n:
        s=s+i
    if noe>0:
      return s/noe
    else:
       return "No elements found"
x=avg(12,34)
print("Avarage is - ",x)