
def lengthDict(line):
    d= {}
    words= line.split()
    for word in words:
        length= len(word)
        if length not in d:
            #add a pair
            d[length]=1
        else:
            #add one to the value associated with key
            d[length]+=1
    return d 
    

print(lengthDict('it is what it is it is python'))
