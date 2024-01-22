'''
Write a function that tells you the odd numbers in a list.
'''

inpList=[]
quantity= int(input("How long do you want your list to be? "))

for i in range(quantity):
    number=int(input("Enter a number: "))
    inpList.append(number)

def findOdds(numList):
    oddNums= []
    for i in numList:
        if i%2==1:
            oddNums.append(i)
    return oddNums
print("Your list of numbers is:", inpList)
answer= findOdds(inpList)
print("The odd numbers in inpList are:", answer)

'''
Write a function that tells you the initials of students in a list
'''
size = int(input('How many names do you want to enter? '))
namesList = []
for i in range(size):
        names = str(input("Enter a name: "))
        namesList.append(names)
print("Your list of names is:", namesList)
def getInitials(nameList):
    initials=''
    for name in namesList:
        initials= initials + name[0]
    return initials
answer2= getInitials(namesList)
print("The initials are:", answer2)
