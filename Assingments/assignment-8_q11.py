print(" cheack they are same in any order or not. ")
a=eval(input("enter the values of first tupple - "))
b=eval(input("enter the values of second tupple - "))
for i in b:
    if i in a:
        pass
    else:
        print("not a subset")
        break
print("second one is a subset of first tuple")