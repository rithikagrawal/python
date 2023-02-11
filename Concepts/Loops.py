# Write a program to print multipliation table of a given number using for loop.

num = int(input("Enter a Number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num*i)

# Write a program to greet all the person names stored in a list L1 and starts with "S".

l1 = ["Harry", "Soham", "Sachin", "Aniket", "Shivam", "Rahul", "Saurabh"]

for item in l1:
    if (item.startswith("S")):
        print("Hello", item)

# Write a program to print multipliation table of a given number using while loop.

num = int(input("Enter a number: "))
i = 1
while (i <= 10):
    print(f"{num} x {i} = {num*i}")
    i += 1

# Write a program to find whether a given number is prime or not?

num = int(input("Enter a number: "))
i = 2
while (i < num):
    if (num % i == 0):
        print(f"{num} is not a Prime Number")
        break
    i += 1
else:
    print(f"{num} is a Prime Number")

# Write a program to find sum of n natural numbers using while loop.

num = int(input("Enter a Number: "))
n = num
sum = 0
while (n > 0):
    sum = sum + n
    n -= 1
print(f"The sum of first {num} natural numbers is {sum}")

# Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter a number: "))
n = num
fact = 1

for i in range(n):
    fact = fact*(i+1)
print(f"The factorial of {n} is {fact}")

# Write a program to print the following star pattern:
#   *
#  ***
# *****

num = int(input("Enter a number: "))

for i in range(1, num+1):
    for j in range(0, num-i):
        print(" ", end="")
    for k in range(0, 2*i-1):
        print("*", end="")
    for l in range(0, num-i):
        print(" ", end="")
    print("\n", end="")

# Write a program to print the following star pattern:
# *
# **
# ***

num = int(input("Enter a number: "))

for i in range(1, num+1):
    for j in range(i):
        print("*", end="")
    print("\n", end="")

# Write a program to print the following star pattern:
# ***
# * *
# ***

num = int(input("Enter a number: "))


for i in range(num):
    for j in range(num):
        if (i == 0 or j == 0 or i == num-1 or j == num-1):
            print("*", end="")
        else:
            print(" ", end="")
    print("\n", end="")

# Write a program to print multiplication table of a number using for loop in reverse order.

num = int(input("Enter a number: "))

for i in range(10, 0, -1):
    print(f"{num} x {i} = {num*i}")
