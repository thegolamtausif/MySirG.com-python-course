def ltf(l):
    dis=dict()
    temp=[]
    for i in l:
        alpha=i[0:1]
        for key,value in dis.items():
            if key==alpha:
               temp=value
               temp.append(i)
               dis[alpha]=temp
               break
        else:
            li=[i]
            dis[alpha]=li
    return dis
lis=["golam","tausif","halima","tawhid","tehran","hasini","hello"]
x=ltf(lis)
for u in x:
    print("key is = ",u,"and value is = ",x[u])