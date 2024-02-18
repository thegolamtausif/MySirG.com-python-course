s1=set(eval(input("enter the first set - ")))
s2=set(eval(input("enter the second set - ")))
cart=set()
for i in s1:
    for j in s2:
        cart.add(i*j)
    print(cart)
    cart.clear()
    