Money=int(input("How much money do you have: "))
Candy=0
for i in range(Money, 0, -4):
    Candy+=1
    if Candy%3==0:
        Candy+=1
print(f"You can purchase {Candy} candy bars!")