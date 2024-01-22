def phoneswithGivenArea(phoneLine, areaCode):
    myList= []
    phone = phoneLine.split(',')
    for number in phone:
        if number[0:3] == areaCode:
            myList.append(number)
    return myList

print(phoneswithGivenArea("956-987-9887,929-370-1741,956-452-8674", "956"))


def firstWithA(names):
    nameList= names.split()
    for name in nameList:
        if 'a' in name.lower():
            return name

print(firstWithA('Kruti Joseph Trisha Alan Jonathan'))


def wordsStats(paragraph):
    wordsPerLine=[]
    linesList= paragraph.split('\n')
    for line in linesList:
        wordsList= line.split()
        length= len(wordsList)
        wordsPerLine.append(length)
    return wordsPerLine

print(wordsStats('it is what it is\npython is fun\nhave a nice spring break'))
