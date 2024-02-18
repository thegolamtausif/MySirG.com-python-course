print("number of days in a month")
x=int(input("enter the month number - "))

if x in (1,3,5,7,8,10,12):
    print("number of days in %d month is - 31 "%x)
elif x in (4,6,9,11):
    print("number of days in %dth month is - 30 "%x)
elif x==2:
    print("number of days in %d month is - 28/29(if leap year)"%x)
else:
    print("invalid month")