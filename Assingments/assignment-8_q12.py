
x=eval(input("enter the values of tupple - "))
same=()
for i in x:
    if str(i) not in same:
      same = same + tuple(str(i))
      c= x.count(i)
      print("count of ",i," is - ",c)
      c=0
