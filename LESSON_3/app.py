## Lesson-3.1 Formatted String
first = 'Khaled'
last = 'Ali'
## Classic string format
message = first + ' [' + last +'] is a coder'
print(message)
## Python better string format
msg = f'{first} [{last}] is a coder'
print(msg)

## Lesson-3.2 String mainpulation
## Getting String lenght using built in 'len' function
course = 'Python for Beginners'
print(len(course))

## dot operator methods
## upper case method
print(course.upper())

## lower case method
print(course.lower())

## find method
print(course.find('P'))

## replace string method
print(course.replace('Beginners', 'Absolute Beginners'))

## title string method
print(course.title())

## "in" operator
print('Beginners' in course) ## Returns a  True boolean value

## "in" operator
print('beginners' in course) ## Returns a  False boolean value