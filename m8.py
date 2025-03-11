#Flatten function
def flatten(inputlist):
    def InnerFlatten(innerlist):
        for j in innerlist:
            if type(j) == list:
                InnerFlatten(j)
            else:
                ReturnList.append(j)
    ReturnList = []
    for i in inputlist:
        if type(i) == list:
            InnerFlatten(i)
        else:
            ReturnList.append(i)
    return ReturnList

#Recursion/Loop Conversion function 1
def mystery1(n):
    a, b, c, d, e = 1, 2, 3, 4, 5
    while n > 0:
        n -= 1
        a, b, c, d, e = b, c, d, e, a-c+e
    return a

#Recursion/Loop Conversion function 2
def mystery2(number):
    def inner(number, digit, total):
        if number // 10 <= 0:
            return total
        return inner(number // 10, number % 10, total + (number % 10))
    return inner(number, number % 10, number % 10)

def mystery3(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

#Collatz Sequence function
def collatz_sequence(n):
    def inner(n):
        if n % 2 == 0:
            print(f"{n:.0f}", end=" ")
            return collatz_sequence(n / 2)
        elif n == 1:
            print(1)
            return 1
        else:
            print(f"{n:.0f}", end=" ")
            return collatz_sequence(3 * n + 1)
    if n % 2 == 0:
        print(f"{n:.0f}",end=" ")
        inner(n / 2)
    elif n == 1:
        print(1)
    else:
        print(f"{n:.0f}",end=" ")
        inner(3 * n + 1)
