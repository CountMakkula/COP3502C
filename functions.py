def sum(*args):
    Sum=0.0
    for i in args:
        Sum=Sum+i
    return Sum

def print_range(start, end):
    i=start
    while end>start:
        print(i, end=", ")
        end-=1
        i+=1
    print(i)

def sum_of_digits(num):
    NumStr=str(num)
    Sum=0
    for i in NumStr:
        Sum=Sum+int(i)
    return Sum