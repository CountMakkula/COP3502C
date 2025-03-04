#Data parsing function
def parse_student(data):
    StudentInfo = {}
    StudentInfo["id"] = data[:8]
    i = 0
    for index, value in enumerate(data[8:]):
        if str(value) == "0" or str(value) == "1":
            StudentInfo["name"] = data[8:index+8]
            i = index+8
            break
    StudentInfo["birthdate"] = str(data[i:i+2]) + "/" + str(data[i+2:])
    return StudentInfo

#List counting function
def count_items(list):
    ItemDictionary = {}
    for i in list:
        ItemDictionary[i] = 0
    for i in list:
        if i in ItemDictionary.keys():
            ItemDictionary[i] += 1
    return ItemDictionary

#List fighters function
def list_fighters(data):
    SortedSet = set()
    for key in data.keys():
        SortedSet.add(key)
        for value in data[key].values():
            for i in value:
                SortedSet.add(i)
    SortedSet = list(SortedSet)
    SortedSet.sort()
    return SortedSet