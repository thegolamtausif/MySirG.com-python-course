class student:
     def __init__(self,name,roll):
          self.name=name
          self.roll=roll
l=[student("golam",18),student("asim",10)]
def savedata():
     import pickle
     f1=open('file2.obj','wb')
     for s in l:
          pickle.dump(s,f1)
     f1.close()
def seedata():
     import pickle
     f2=open('file2.obj','rb')
     e_list=[]
     while True:
          try:
               e_list+=[pickle.load(f2)]
          except EOFError:
               break
     return e_list
savedata()
l=seedata()
for e in l:
     print(e.name,e.roll)