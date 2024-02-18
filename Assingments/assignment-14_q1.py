class student:
    
    def __init__(self,n):
        self.n=n
        print("Enter details for obj no - ",self.n)
        self.rollno=int(input("Enter rollno - "))
        self.name=(input("Enter  name - "))
        self.semester=int(input("Enter current semester - "))
        self.branch=(input("Enter  branch name- "))
    def pdetails(self):
        print("Printing details of  obj no - ",self.n)
        print("name is -",self.name)
        print("rollno is -",self.rollno)
        print("semester is -",self.semester)
        print("branch name  is -",self.branch)
golam=student(1)
asim=student(2)
golam.pdetails()