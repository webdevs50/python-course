## Functions
## To define a a function in Python we start with 'def" keyword followed by function name, parentces and colon.
def greet_user():
    print('Hi there!')
    print('Welcome aboard')


print("Start")
greet_user()
print("Finished")
print("\n\n")

## Passing Parameters to a Function
def greet_user_by_name(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user_by_name("Marwan", "Ali") ## Positional arguments
greet_user_by_name("Dareen", "Khaled")  ## Positional arguments
print("Finished")

## Keyword Arguments. Using keyworg argument does not require us to maitaine the order 
# of the parameters in the function signature

print("Start Keyword Arguments")
greet_user_by_name("Marwan", "Ali") ##  ## Positional arguments. Order maters
greet_user_by_name(last_name="Khaled", first_name="Dareen") ## Keyword arguments. Order Does not mater. Improves code readability
print("Finished")

print("Mixed Keyword Arguments and positional Order")
greet_user_by_name("Marwan", last_name="Ali") ##  ## Positional arguments should be always before keyword argument
print("Finished")


## Functions that Return values
# By default a function return none
def square(number):
    return number * number

print(square(4))


## Reusable Functions
def emoji_util(message):
    words = message.split(" ")
    emojis = {
        ":)": "😁",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " " 
    return output



message = input("> ")   
my_state = emoji_util(message)
print(my_state)