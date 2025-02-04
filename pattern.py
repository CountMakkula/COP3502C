Height=int(input("Height: "))
for i in range(1, Height+1):
    n=1
    for j in range(1, Height+1):
        if i+j>=Height+1:
            print(n, end="")
            n=n+1
        else:
            print(" ", end="")
    print()