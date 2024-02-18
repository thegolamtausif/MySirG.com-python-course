print("File handling")
f=open("file.txt","w")
l=["golam\n","tausif\n","halima\n"]
f.writelines(l)
f.close()
f=open("file.txt","r")
"""
for line in f:
    print(line,end=" ")
while True:
   s=f.readline()
   if s == '':
      break
   print(s)
"""
s1=f.readlines()
print(s1)
f.close()