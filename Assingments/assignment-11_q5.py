def coe(*n):
    sodd = 0
    seven = 0
    for i in n:
        if i%2 == 0:
            seven = seven + i
        else:
            sodd = sodd +i
    return sodd,seven
x,y=coe(10,12,13,26,29)
print("Sum of all odd number is %d and \nsum of all even number is %d"%(x,y))