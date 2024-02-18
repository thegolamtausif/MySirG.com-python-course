class person:
    def __init__(self,n,a):
     self.name=n
     self.age=a
class student(person):
   def __init__(self,r,n,a):
      self.roll=r
      person.__init__(self,n,a)
class teacher(person):
    def __init__(self,i,n,a):
        self.id=i
        person.__init__(self,n,a)
class broghtstudent(student,teacher):
    def __init__(self,p,i,r,n,a):
        self.points=p
        student.__init__(self,r,n,a)
        teacher.__init__(self,i,n,a)
obj=broghtstudent(200,20010,18,"golam",21)
print(obj.__dict__)