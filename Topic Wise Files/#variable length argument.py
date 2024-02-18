#variable length argument
def  abc(a,*b):
    print(a,end=' ')
    s=0
    for i in b:
        s=s+i
    print(" , total point=",s)

abc("golam",12,12,13)