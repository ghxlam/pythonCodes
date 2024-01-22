class Point:
    '''this class defines a point'''

    def __init__(self, x_coor, y_coor):
        self.x = x_coor
        self.y = y_coor

    def getCoordinates(self):
        '''returns the coordinates of self (3,5) as a tuple'''
        return (self.x, self.y)

    def move_to(self, newX, newY):
        '''assign new coordinates to a point'''
        self.x = newX
        self.y = newY

    def distance_to(self, other):
        import math
        dist = math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        return dist
