'''
Write a program that creates a list of 5 exam scores by adding them
one at a time
The Program calculates and prints to the screen:
1. The average exam score
2. The min score
3. The max score
4. The number of perfect scores in the list 100s

examScores = []
examScores.append(100)
examScores.append(95)
examScores.append(65)
examScores.append(85)
examScores.append(100)
print("Your average exam score is: ", sum(examScores)/len(examScores))
print("Your lowest exam score is: ", min(examScores))
print("Your highest exam score is: ", max(examScores))
print("The amount of times you got a perfect score: ", examScores.count(100))
'''
'''
p1= ['do', 'it', 'better']
p2= ['make', 'us', 'stronger']

newList= (p2[0:1]+p1[1:2]+p1[2:])
print(newList)
'''
message = 'therefore the python language is the best'
message.count('the')

