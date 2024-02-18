#next prime number of a given number 
def npg(g):
    b=0
    for i in range(g+1,10000000):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            b+=1
            return i
        if b>0:
            break
np=npg(17)
print(np)
        
