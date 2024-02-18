n=int(input("enter the size of the list - "))
l=[]
for i in range(n):
      l.append(int(input("enter a number -")))
sum_odd=0
sum_even=0
for i in range(n):
      if l[i]%2==0:
            sum_even = sum_even + l[i]
      else:
            sum_odd = sum_odd + l[i]
print("sum of all odd number is - ",sum_odd)
print("sum of all even number is - ",sum_even)
