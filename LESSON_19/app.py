## Generating Randon Values
## Python has several builtin modules such as random module for generating random numbers
import random

for i in range(5):
    print(random.random())

## If we want a randon number between two int value we can use randint function
for i in range(5):
    print(random.randint(5, 25)) ## Genertes random int numbers between 5 and 25

## If we wnat to select a random value from a list we can use the choince function from random module

members = ['Khaled', 'Mohamed', 'Muizz', 'Marwan', 'Soadd', 'Danya', 'Duja', 'Dareen']

for i in range(6):
    print(random.choice(members))

## Excersie: Write a programm to roll a dice and get tuble of two values

class Dice:
    def __random_num(self):  ## In python, a private function is defined by starting the function name  by two underscors
        return random.randint(1, 6)
    
    def roll(self):
        return self.__random_num(), self.__random_num()


dice = Dice()
print(dice.roll())