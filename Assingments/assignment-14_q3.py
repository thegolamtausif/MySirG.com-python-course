class employee:
    def __init__(self):
        self.name=(input("Enter the name of the employee -"))
        self.empid=int(input("Enter the empid of the employee -"))
        self.salary=int(input("Enter the salary of the employee -"))
    def display(self):
        print("NAME IS - ",self.name)
        print("EMPID IS - ",self.empid)
        print("SALARY IS - ",self.salary)
    def sort_by_name(a,b,c):
        l=[a.name, b.name, c.name ]
        l.sort()
        for i in l:
            for x in (a,b,c):
                if i==x.name :
                    x.display()
    def sort_by_salary(a,b,c):
        l=[a.salary, b.salary, c.salary ]
        l.sort()
        l.reverse()
        for i in l:
            for x in (a,b,c):
                if i==x.salary :
                    x.display()
a=employee()
b=employee()
c=employee()
a.sort_by_name(b,c)
a.sort_by_salary(b,c)

