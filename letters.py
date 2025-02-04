Word=input("Enter a word: ")
Letter=input("Enter the letter to count: ")
Count=0
for i in Word:
    if i == Letter:
        Count+=1
print(f"{Letter} appears {Count} times.")