## Constructors
## A constructor is a special function called at the time of creatting an object of a class
## We can pass attributes to a class to initialize the created objecy
## For example, for a Point class, we can pass the x and y value to a class

class Point:
    def __init__(self, x, y): ## __init__ is the constructor method. self is a reference to the current object
        self.x = x
        self.y = y

    def move(self): # each method has to has self argument
        print('Move Point')
    
    def draw(self):  # each method has to has self argument
        print('Draw Point')

point1 = Point(44, 66)
print(point1.x)

## Also, we can change the value of an attribute
point1.x = 55
print(point1.x)

## Test
## Create a Person class that has a name attribute and talk method
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self, speech):
        print(f'{self.name} speaks {speech}')


Khaled = Person('Khaled Ali')

print(Khaled.name)
khaledLang = Khaled.talk("Arabic")
print(khaledLang)

## Inheritance
## In Inheritance, we define a class which has a common methods to other class.
## Other classes inherit that method from the super class

class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def meo(self):
        print("meo meo")


my_cat = Cat()

my_cat.walk()
my_cat.meo()