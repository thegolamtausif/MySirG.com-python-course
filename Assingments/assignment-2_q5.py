print("cheack if a year is leap year or not")
x=int(input("enter the year -"))


if (x%400==0) or (x%100!=0) and (x%4==0):
    print("%d is a leap year."%x)
else:
    print("%d is not a leap year."%x)