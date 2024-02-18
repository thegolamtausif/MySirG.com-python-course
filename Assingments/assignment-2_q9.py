print("find the grater between real part and imaginary part of a complex number .")
x=complex(input("enter a complex number - "))
y=x.real
z=x.imag
if y>z:
    print("the real part is bigger")
elif z>y:
    print("the imag part is bigger")
