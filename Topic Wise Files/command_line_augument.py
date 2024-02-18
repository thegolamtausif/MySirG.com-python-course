from sys import argv
sum=0
y=0
for x in argv:
    if y==0:
       y=1
    else:
       sum = sum + int(x)
print("sum is - ",sum)