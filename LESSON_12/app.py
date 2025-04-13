## List Methods
numbers = [5, 2, 1, 7, 8]
print(numbers) ## [5, 2, 1, 7, 8]

## Adding a number to a list
numbers.append(30)
print(numbers) ## [5, 2, 1, 7, 8, 30]

## Inserting a number at a specific position in a list
## list.insert(index, value)
numbers.insert(3, 55)
print(numbers) ## [5, 2, 1, 55, 7, 8, 30]

## Removing a number from a list
## list.remove(value)
numbers.remove(1)
print(numbers) ## [5, 2, 55, 7, 8, 30]

## Removing all numbers in a list
## list.clear(value)
numbers.clear()
print(numbers) ## []

## Removing last item in a list
## list.pop()
numbers = [5, 2, 1, 7, 8]
numbers.pop()
print(numbers) ## [5, 2, 1, 7]

## Returing the index of the first occurnce of an item in a list
## list.index(value)
print(numbers.index(2)) ## 1

## Checking the existins of an item in a list
print(7 in numbers) ## True
print(20 in numbers) ## False

## Checking the number of occurances of an item in a list
numbers = [5, 2, 1, 2, 2,  7, 8]
print(numbers.count(2)) ## 3


## Sorting item in a list
numbers = [5, 2, 1, 2, 2,  7, 8]
numbers.sort()
print(numbers) ## [1, 2, 2, 2, 5, 7, 8] ASC

## Coping a list
numbers_Copy = numbers.copy()
print(f"Copied List: {numbers_Copy}")

## Sorting in DSC
numbers_Copy.reverse()
print(numbers_Copy) ## [8, 7, 5, 2, 2, 2, 1] DSC
