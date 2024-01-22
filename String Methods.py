msg= 'hello there how are you'
wordsList= msg.split()
count=0
print(msg)
print(wordsList)
print(len(wordsList))
for word in wordsList:
    if word[-1] in 'aeiou':
        count= count+1
print(count)
