## Lesson-4.1 Python Arthmetic Operators
## Addition
print(10 + 3)

## Subtraction
print(10 - 3)

## Multiplaction
print(10 * 3)

## Division
print(10 / 3) ## We get a floating number of this

print(10 // 3) ## We get an integer number of this

## Modular
print(10 % 3) ## We get remainder of this


## exponent
print(10 ** 3) ## We get power of a number

## Augmented Assignemnt  Operator
x = 10
x = x + 3  # Classic Way
print(x)

## Augmented Way

x += 3
print(x)

x -= 3
print(x)

x *= 3
print(x)

x /= 3
print(x)

## Lesson-4.2 Python Operators precedence 
x = 10 + 3 * 2  ## multiplication has higher precedence then addition. The result of will be 16
print(x)

## In python same as for other language, the operators precedence are as below:
## exponentiation   2 ** 3
## multiplication or division
## addition or subtraction

x = 10 + 3 * 2 ** 2  ## x will be 22
print(x)


## Lesson-4.3 Changing the order of Operators precedence using parenthesis 
## Operations inside parenthesis always has higher priorities
x = (10 + 3) * 2 ** 2  ## x will be 52 since the first operation will be (10 + 3)
print(x)