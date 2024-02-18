print("enter a  odd number to win . you have 3 chances.")
chance=3
while chance>0:

   x=int(input("enter a number - "))
   if x%2==0:
      break
   chance-=1
if chance==0:
   print("you lost ")
else:
   print("you win ")