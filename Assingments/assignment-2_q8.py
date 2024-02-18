print("print words in dictionary order")
x=input("enter first word - ")
y=input("enter second word - ")
z=input("enter third word - ")
print("printing given words in dictionary order .....")
if x>y : 
    if x<z:
        print(y,x,z,sep="\n")
    elif x>z :
        if z<y:
            print(z,y,x,sep="\n")
        elif z>y:
            print(y,z,x,sep="\n")
elif y>x:
    if y<z:
        print(x,y,z,sep="\n")
    elif y>z :
        if z<x:
            print(z,x,y,sep="\n")
        elif z>x:
            print(x,z,y,sep="\n")