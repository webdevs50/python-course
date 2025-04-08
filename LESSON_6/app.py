## LESSON 6: Python Condition Statments

## LESSON 6.1: If Statments
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm cloths")
else:
    print("It's a lovely day. Enjoy your day!")

## Example
## Give a house price of a $1M. If buyer has a good credit, 
# they need to put 10% as a down payment. Otherwise, 
# they need to put a 20% down payment. Print the down down payment.

is_Good_Credit = True
price = 1000000

if is_Good_Credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down payment: ${down_payment}")


## LESSON 6.2: Logical Operators
## Logical Operator AND
## Ex: If an applicant has high income and good credit then he/she is eligible for loan
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

## Logical Operator OR
## Ex: If an applicant has high income or good credit then he/she is eligible for loan
has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for loan")

## Logical Operator Not
## Ex: If an applicant has good credit and he/she doesn't have a criminal records then he/she eligible for loan
has_good_credit = True
has_criminal_records = False

if has_good_credit and not has_criminal_records:
    print("Eligible for loan")

## LESSON 6.3: Comparison Operators
##  >, >=, <, <=, ==, !=
temperature = 30

if temperature >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

## Ex
## We need to validate the name to be at least 3 character and less tne 50 characters
name = "KHALED"
nameLen = len(name)
if nameLen < 3:
    print("Name must be at least 3 characters")
elif nameLen > 50:
    print("Name must less then or equal to 50 charcters")
else:
    print("Name lenght is good :)")
