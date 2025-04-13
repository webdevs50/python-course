## Tuples
## Tuples like lists where we can store a list of items. Tuples are not like lists where we
## can not modify Tuples. There are only two methods in Tuples: Count and Index methods.

numbers = (1, 2, 3, 4, 5)
print(numbers.count(2)) 

print(numbers.index(4))


## UnPacking
## If we need to get the values of a tuple to be assigned to varaibles we can do it like:
coordinates = (33, 55, 66)
x, y, z = coordinates

print(x, y, z)


## Dictionaries
## When we need to store information as Key-Value paries, we use disctionaries. Dictornaries 
# are like objects in JavaScript.
customer = {
    "name": "Khaled Ali",
    "age": 55,
    "is_verified": True
}

print(customer["name"])

## If we use a key doesn't exist and try to get it using [key] we will get an error.
## To avoid such error we need to use get method
### print(customer["DoB"]) ## Give an error

print(customer.get("DoB")) ## none

## If the object does not have such key, we can have a default value
print(customer.get("DoB", "Jan 10, 1970")) ## Jan 10, 1970


## We can update the value of any key in an object
customer["name"] = "Khaled Amer Ali" 
print(customer) ## {'name': 'Khaled Amer Ali', 'age': 55, 'is_verified': True}

## Excersise: Translate numbers to works
numbers_words = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six"
}

phone = input("Phone: ")
words = ""
for digit in phone:
    words += numbers_words[digit]
    words += " "
print(words)

## Repalcing emojis chaecters with emojis
emojis = {
    ":)": "😁",
    ":(": "😔"
}

message = input("> ")
words = message.split(" ")
output = ""
for word in words:
   output += emojis.get(word, word) + " " 
print(output)