#define a new function/ create a new function
def f(x):
    result= x**2 + 1
    #print(result)
    return result

#use (call) functions
print(f(2))

answer=f(1)
print(answer)

print(f(2)+2*f(1))
'''
def hello(name):
    line= "Welcome, "+name+", to the world of python"
    print(line)
name= str(input("What is your name?"))
hello(name)
    '''
#define the function oddCount()
quantity= int(input("How many numbers do you want in the list? "))
lst1=[]
for i in range(quantity):
    number= int(input("Enter a number: "))
    lst1.append(number)
print("Your List is ", lst1)
def oddCount(numberList):
    count=0
    for number in numberList:
        if number%2==1:
            count=count+1
    return count
print(oddCount(lst1))
