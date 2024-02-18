class employee:
    empid=0
    name="S"
    salary=0
    def __init__(self,a,b,c):
        self.empid=a
        self.name=b
        self.salary=c
    def display(self):
        print("NAME IS - ",self.name)
        print("EMPID IS - ",self.empid)
        print("SALARY IS - ",self.salary)
a=employee(210018,"golam",930000000)
b=employee(210010,"asim",95000)
a.display()
b.display()
