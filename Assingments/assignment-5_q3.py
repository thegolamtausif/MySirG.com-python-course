print("all amostrong number under 1000")
z=0
for i in range(1,1000):
    a=i
    for j in range(100,1,-90):
        x=a//j
        z=z+x**3
        a=a%j
    z=z+a**3
    if i==z:
      print(z)
    z=0

