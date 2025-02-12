#Function 1: Fibonacci Sequence
def fibonacci(position):
    result=0
    start1=0
    start2=1
    for i in range(0, position-1):
        if i%2==0:
            start2+=start1
            result=start2
        elif i%2!=0:
            start1+=start2
            result=start1
    return result

#Function 2: Prime numbers
def is_prime(num):
    if num<=0 or num==1:
        return False
    for i in range(2, 8):
        if num%i==0 and num/i>1:
            return False
    return True

#Function 3: Prime Factorization
def print_prime_factors(num):
    print(f"{num} =", end=" ")
    for i in range(1, num+1):
        if is_prime(i) and num%i==0:
            while num%i==0:
                print(i, end="")
                num=num/i
                if num == 1 and i!=num:
                    break
                print(" * ", end="")