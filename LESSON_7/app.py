## Write a program to convert weight based on the unit provided
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")


## While Loops
i = 0
while i <= 5:
    print('*' * i)
    i +=1
print("We are Done....")

## Building a Gussing game using While Loop
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You Won! ')
        break
else:
    print('Sorry, you failed!')
