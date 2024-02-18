class person:
    def __init__(self,a,b):
        self.name=a
        self.age=b
    def display(self):
        print("name is - ",self.name)
        print("age is - ",self.age)
class student(person):
    def __init__(self,n,x,y):
        self.roll=n
        #person.__init__(self,x,y)
        super().__init__(x,y)
    def display1(self):
        print("roll is - ",self.roll)
s1=student(23,"golam",18)
print(s1.__dict__)
s1.display1()
s1.display()