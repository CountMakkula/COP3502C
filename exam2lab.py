#Backwards string function
def print_backwards(string):
    if len(string) <= 1:
        print(string,end="")
    else:
        print(string[-1],end="")
        print_backwards(string[:-1])

#Name format function
def format_names(namelist):
    ReturnList = []
    def inner(namelist2):
        if "," in namelist2[0]:
            ReturnList.append(namelist2[0])
        else:
            SplitIndex = namelist2[0].index(" ")
            FormattedName = namelist2[0][SplitIndex+1:] + ", " + namelist2[0][:SplitIndex]
            ReturnList.append(FormattedName)
        if len(namelist2) > 1:
            inner(namelist2[1:])
    inner(namelist)
    return ReturnList

#Dictionary sum function
def sum_a(data):
    if len(data) <= 1:
        if "a" in data[0].keys():
            return data[0].get("a")
        else:
            return 0
    if "a" in data[0].keys():
        return sum_a(data[1:]) + data[0].get("a")
    else:
        return sum_a(data[1:])

#List processing function
def process_list(numberlist):
    ReturnList = []
    def inner(index):
        if index > len(numberlist) - 1:
            if index % 2 == 0:
                inner(1)
                return ReturnList
            else:
                return ReturnList
        if index % 2 == 0:
            ReturnList.append(str(numberlist[index]))
            inner(index+2)
        else:
            ReturnList.append(numberlist[index] * 10)
            inner(index+2)
    inner(0)
    return ReturnList
