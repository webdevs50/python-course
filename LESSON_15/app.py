## Exceptions
## Exceptions is used to handle errors in python programs

try:
    age = int(input("Age: > "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')