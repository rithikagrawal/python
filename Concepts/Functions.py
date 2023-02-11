# Function

def avg(a, b, c):
    return ((a+b+c)/3)


print(avg(10, 20, 30))

# Function with default argument/parameter


def greet(name="Ankit"):
    print("Hello", name)


greet("Rithik")

# Recursion


def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n*factorial(n-1)


n = int(input("Enter a Number:"))
print(f"Factorial of {n} is:", factorial(n))

#  Write a program using function to find greatest of three numbers


def greatestOfThreeNum(a, b, c):
    if (a > b):
        if (a > c):
            return a
    elif (b > a):
        if (b > c):
            return b
    return c


num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

print(f"The greatest of {num1},{num2} & {num3} is:",
      greatestOfThreeNum(num1, num2, num3))


# Write a python program using function to convert Celsius to Fahrenheit.

# Formula: F = C X 9/5 + 32

def celsiusToFahrenheit(num):
    return ((num*9)/5)+32


num = float(input("Enter temperature in degree Celsius: "))

print(f"{num} 'C = {celsiusToFahrenheit(num)} 'F")

# How do you prevent a python print() function to printa new line at the end.

# Solution: Using the end=""

print("Hello World!!", end=" ")
print("Hello World again!!")

# Write a recursive function to calculate the sum of first n natural numbers.


def sum(num):
    if (num == 1):
        return num
    else:
        return num + sum(num-1)


num = int(input("Enter n: "))
print(f"The sum of first {num} Natural Numbers is: {sum(num)}")

# Write a python function to print fisrt n lines of the following pattern:

# ***
# **
# *


def pattern(num):
    for i in range(num):
        print("*"*(num-i))


pattern(int(input("Enter a number: ")))

# Write a python function which converts inches to cms


def inchToCms(num):
    return num*2.54


print(f'{inchToCms(float(input("Enter value in inch: ")))} Centimetres')

# Write a python function to remove a given word from a list and strip it at the same time.


def removeFromList(l, word):
    word = word.strip()
    if word in l:
        l.remove(word)
    return l


ls = ['diffraction', 'stf'
      'oli',
      'sint',
      'wie',
      'decks',
      'leans',
      'amp',
      'ordinate',
      'preview']

word = input("Enter a word to be removed from the list: ")

print("After removal list is:", removeFromList(ls, word))

# Write a python program to print multiplication table of a given number.


def printTable(num):
    for i in range(10):
        print(f"{num} X {i+1} = {num*(i+1)}")


num = int(input("Enter a number: "))

printTable(num)
