import math
#Fourbonacci sequence function
def fourbonacci(n):
    result=0
    start=[1,4,7,8]
    if n>4:
        for i in range(5, n+1):
            result=4*start[0]+3*start[1]+2*start[2]+start[3]
            start.append(result)
            start.pop(0)
        return result
    else:
        return start[n-1];

#Odd squares function
def odd_squares(n):
    i=0
    num=1
    while i<n:
        if math.sqrt(num)==math.isqrt(num) and num%2!=0:
            print(num)
            i+=1
            num+=1
        else:
            num+=1

#Diamond function
def diamond(height):
    #Rows
    mid=math.ceil(height/2)+1
    midMatrix=mid
    fill=0
    for i in range(1,height+1):
        num=1
        #Columns
        for j in range(1, height+1):
            if (i+j>=mid-fill) and (i+j<=mid+fill):
                print(num, end="")
                num+=1
            else:
                print(" ", end="")
        mid+=1
        if i < midMatrix - 1:
            fill += 1
        else:
            fill -= 1
        print()