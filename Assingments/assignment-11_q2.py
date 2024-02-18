def revbin(num):
    binum=list(bin(num)[2::])
    print("Reversed binary of %d is"%num,end=" ")
    binum.reverse()
    for i in binum:
        print(i,end="")
revbin(23)