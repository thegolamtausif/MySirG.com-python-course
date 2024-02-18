print(" calculate avarage of tupl values. ")
x=eval(input("enter the values of tupple - "))
y=()
homo=()
j=0
for i in x:
     if str(i) in y and str(i) not in homo:
        homo = homo + tuple(str(i))
     elif str(i) not in homo:
        y=y+tuple(str(i))
print("heteregenous tuple is  - " ,y)
print("homogeneous tuples are - " ,homo)