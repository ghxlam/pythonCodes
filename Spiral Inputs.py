'''
line=lineInitial= int(input("What is the Initial Line: "))
change= int(input("How much does each line increase by: "))
angle= int(input("What is the angle in between in each line: "))
lines= int(input("How many lines should the turtle draw: "))
import turtle
paper= turtle.Screen()
pen= turtle.Turtle()
'''
def spiral(pen, length, change, lines, angle):
    pen.down()
    for i in range(lines):
        pen.forward(length)
        pen.back(length)
        pen.right(angle)
        length= length+change

import turtle
paper= turtle.Screen()
pen= turtle.Turtle()
spiral(pen, 40, 20, 20, 20)



'''
for i in range(10):
    pen.forward(line)
    pen.back(line)
    pen.right(angle)
    line= line+change
'''
#The original code
'''
pen.forward(line)
pen.back(line)
pen.right(angle)
line= line+change

pen.forward(line)
pen.back(line)
pen.right(angle)
line= line+change

pen.forward(line)
pen.back(line)
pen.right(angle)
line= line+change

pen.forward(line)
pen.back(line)
pen.right(angle)
line= line+change

pen.forward(line)
pen.back(line)
pen.right(angle)
line= line+change

pen.forward(line)
pen.back(line)
pen.right(angle)
line= line+change

pen.forward(line)
pen.back(line)
pen.right(angle)
line= line+change

pen.forward(line)
pen.back(line)
pen.right(angle)
line= line+change

pen.forward(line)
pen.back(line)
pen.right(angle)
line= line+change

pen.forward(line)
pen.back(line)
pen.right(angle)
line= line+change
'''
