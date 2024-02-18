x=input("enter a string - ")
n=len(x)
count=0
for i in range(n):
    if x[i] in ("a","e","i","o","u"):
        count+=1

print("count is - ",count)