# Write a program to print multipliation table of a given number using for loop.

# num = int(input("Enter a Number: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num*i)

# Write a program to greet all the person names stored in a list L1 and starts with "S".

# l1 = ["Harry", "Soham", "Sachin", "Aniket", "Shivam", "Rahul", "Saurabh"]

# for item in l1:
#     if (item.startswith("S")):
#         print("Hello", item)

# Write a program to print multipliation table of a given number using while loop.

# num = int(input("Enter a number: "))
# i = 1
# while (i <= 10):
#     print(f"{num} x {i} = {num*i}")
#     i += 1

# Write a program to find whether a given number is prime or not?

num = int(input("Enter a number: "))
count = 0
i = 2
while (i <= num):
    if (num % i == 0):
        count += 1
    i += 1
if (count == 1):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
