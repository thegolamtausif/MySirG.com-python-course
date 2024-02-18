#variable length keyword argument 
def  abc(**b):
    print("person information ")
    for key,value in b.items():
        print(key,"-",value)
abc(name="golam",roll=18,YOB=2003)