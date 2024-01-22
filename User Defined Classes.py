import point
pointA = point.Point(3,5)
print(pointA.getCoordinates())
pointA.move_to(10,20)
print(pointA.getCoordinates())

origin= point.Point(0,0)
print(pointA.distance_to(origin))
