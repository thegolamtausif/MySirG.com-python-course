print("check the nature of roots of  given quatratic equation . ")
import math
a=float(input("enter the value of a - "))
b=float(input("enter the value of b - "))
c=float(input("enter the value of c - "))
b2=b**2
d=b2-4*a*c
'''
The term b2- 4ac is known as the discriminant
If the discriminant is greater than 0, the roots are real and different.
If the discriminant is equal to 0, the roots are real and equal.
If the discriminant is less than 0, the roots are complex and different.
'''
e=2*a
if d>0: 
    y=math.sqrt(d)
    root1=(-b-y)/e
    root2=(-b+y)/e
    print("discriminant is greater than zero so the roots are real and different. ")
elif d==0:
    root1=-b/e
    root2=root1
    print("discriminant is equal to zero so the roots are real and equal. ")
elif d<0:
    print("discriminant is less than zero so the roots are complex and different. ")
    y=math.sqrt(abs(d))
    root1=complex((-b)/e + (y/e)*1j) 
    root2=complex((-b)/e - (y/e)*1j)
print("root1 is {0} and \nroot2 is {1}".format(root1,root2))
