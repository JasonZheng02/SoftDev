import random
    
def MakeArray():
    array = []
    file = open("notes-and-code19-20/smpl/occupations.csv",'r')
    file.readline()
    for line in file:
        if '"' in line:
            array.append(line.split('"')[1:])
        else:
            array.append(line.split(','))
    array = array[:-1]
    for line in array:
        line[1] = line[1][:-1]
        if ',' in line[1]:
            line[1] = line[1][1:]
    return array

def MakeDict(array):
    dic = {}
    x = round(random.uniform(0,99.8),1)
    y = 0
    for line in array:
        dic[line[0]] = line[1]
        y += float(line[1])
        if y > x:
            return(line[0])

def RandomOccupation():
    print(MakeDict(MakeArray()))
    
RandomOccupation()
