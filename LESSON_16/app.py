# Comments, This is a one line comment
# We can have comments in multiple lines
# Comments should explaine how the program works
print("Comments are used to explained the code functionality")


## Classes in Python

## In Python, classes are defined by using the "class" keyword which defines a blueprint of an object
## We use classes to define new types
## These class can have methods and attributes
## Objects instantiated from these classes contain specific data to data object
class Point:
    def move(self): # each method has to has self argument
        print('Move Point')
    
    def draw(self):  # each method has to has self argument
        print('Draw Point')

point1 = Point()

point1.x = 10
point1.y = 30

print(point1.x) ## Adding attributes to point object
print(point1.y) ## Adding attributes to point object

point1.move()
point1.draw()

## If we create another point object of the class Point will have totally different data
point2 = Point()


point2.x = 5 # Settign the x attribute to point2 to be 5

print(point2.x)  ## x of point 2 has different value then x of point 1

