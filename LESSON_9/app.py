## For Loop
## Looping over string characters
for char in 'Python':
    print(char)


## Looping over a list of items
for fruit in ["Apple", "Orange", "Peach", "Watermellon", "Kewi"]:
    print (fruit)

## Looping over a list of numbers
for num in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(num)

## Range Functions
for num in range(10):
    print(num)


## Range Functions Starting from number X ends on 10
for num in range(5, 10, 2):
    print(num)

## Exc. Calculate the total cost of items on a shopping Cart
total_price = 0
prices = [10, 15, 20, 40, 85, 22]

for price in prices:
    total_price += price
print(f"Total Price: {total_price}")



