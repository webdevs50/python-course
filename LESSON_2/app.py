## Lession 2: Getting input from user and Type Conversion in Python

name = input('Enter you name: ')
print('Hi, ', name)

fav_color = input('Enter your fav. color: ')
print(name, 'likes', fav_color)


## Type Conversion
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2025 - int(birth_year)
print(type(age))
print('You age is: ', age)

## Coverting Lbs to Kgs
conversion_rate = 0.453

weight_lbs = input('Enter weight in lbs ')
weight_kgs = float(weight_lbs) * conversion_rate

print(weight_lbs, 'lbs, equals ', weight_kgs, ' kgs')

## Adding specail charcters
course = "Python's for Beginners"
print(course)


## Multiple lines strings 
multi_line_string = '''
Hello, this is Khaled Ali,
I am from Libya,
I live in USA
I do software development
'''

print(multi_line_string)

## Getting String Charcters using the String Index

course = 'Python for Beginners'
print(course[0])  ## Prints the charcter at position zero "P"
print(course[-1]) ## Prints the charcter at last position
print(course[1:4]) ## Prints the charcters from last postion till the third position but not the one at position -4 "ers"