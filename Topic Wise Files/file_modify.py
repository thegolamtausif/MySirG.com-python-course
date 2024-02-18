f=open("file.txt","r+")
x="tausif\n"
l=0
s=f.readline()
while True:
    if s=='':
        break
    l+=len(s)
    if s==x:
        f.seek(l-len(s)+1,0)
        f.write("HALIMA\n")
        break
    s=f.readline()
f.close()