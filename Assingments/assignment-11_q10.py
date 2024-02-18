def ltf(l):
    dis=dict()
    temp=[]
    for i in l:
         if i not in temp:
           n=l.count(i)
           dis[i]=n
           temp.append(i)
    return dis
tup=(1,2,3,2,3,1,5,4,6,1,7,2,8)
x=ltf(tup)
for u in x:
    print("Number is = ",u,"and count is = ",x[u])