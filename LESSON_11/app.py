## Working with Lists
## Printing The whole list
names = ["Khaled", "Amer", "Ali", "Mohamed", "Muizz", "Marwan"]
print(names)

## Printing a single list element using list index
print(names[0])

## Printing a single or multiple list elements using start from index
print(names[2:]) ## Starting from index 2 till the list index

## Printing a single or multiple list elements using start from index and end index
print(names[2: 4]) ## Starting from index 2 till list index 4 but not including index 4

## Printing only lastlist element using start from last index
print(names[-1:]) ## Starting from last index print only last element

## Printing from negative index till last list element
print(names[-3:]) ## Starting from last index print only last element

## Printing from negative index till but not including secoond negative index
print(names[-3: -2]) ## Starting from -3 print till but not including index -2

## Modifying List Elements

## Modefine name at index 2 to be Hassan
names[2] = "Hassan"
print(names) 

## Execericse: Finidng the maximum number in a list

numbers = [5, 4, 22, 13, 45, 78, 90, 32, 134, 564]
maxNumber = 0
for number in numbers:
    if maxNumber < number:
        maxNumber = number
print(maxNumber)


## 2D Lists
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(matrix[1][3])

## Updating an item in 2D List
matrix[0][2] = 6
print(matrix[0][2])

## Looping over 2D Lists using for loop
for row in matrix: ## row is a list of matrix list
    for item in row:
        print(item)
    print("================\n\n")