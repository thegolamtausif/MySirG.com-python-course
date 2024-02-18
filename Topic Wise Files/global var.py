y=10
def f1():

  #  global y

    y=4

    print("inside local ",y)
    print("inside global ",globals()['y'])
f1()
print("outside",y)
