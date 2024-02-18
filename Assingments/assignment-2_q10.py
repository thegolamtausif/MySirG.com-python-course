print("exam")
a=float(input("enter marks - "))
b=float(input("enter marks - "))
c=float(input("enter marks - "))
d=float(input("enter marks - "))
e=float(input("enter marks - "))
sum= a+b+c+d+e
percentage=sum/5
if percentage>40 and a >34.99 and b>34.99 and c>34.99 and d>34.99 and e>34.99:
    print("you passed the exam .")
    print("you get %g percentage marks"%percentage)
else:
    print("you failed in the exam .")