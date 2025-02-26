#Decimal to binary function
def bin(decimal):
    Binary=[]
    ReturnStr=""
    if decimal==0:
        return "0"
    while decimal>=1:
        Binary.append(decimal%2)
        decimal = decimal//2
    for i in Binary[::-1]:
        ReturnStr+=str(i)
    return ReturnStr

#Capitalze function
def capitalize(str):
    NewStr=str.split(" ")
    ReturnList=[]
    ReturnStr=""
    for word in NewStr:
        if word[0].lower() in ["o","u","s","n","d"]:
            ReturnList.append(word[::].lower())
        else:
            ReturnList.append(word[0].capitalize()+word[1:].lower())
    for word in ReturnList:
        ReturnStr+=word
        ReturnStr+=" "
    return ReturnStr[:len(ReturnStr)-1]

#List partition function
numbers = [1,2,3,4,5,6,7,8,9,10]
def partition(list, length):
    NewList=[]
    Bound=length
    BoundUpper=Bound
    Iteration=0
    for i in range(0,len(list), length):
        NewList.append("")
        NewList[Iteration]=[]
        if BoundUpper>len(list):
            BoundUpper=len(list)
        for j in range(Bound-length,BoundUpper):
            NewList[Iteration].append(list[j])
        Bound+=length
        BoundUpper+=length
        Iteration+=1
    return NewList