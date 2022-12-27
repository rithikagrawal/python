# Write a program to store seven fruits in a list eneterd by the user.

fruitList = []
for i in range(7):
    fruitList.append(
        input("Enter the name of fruit to be added in the list: "))
print(fruitList)

# Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []
for i in range(6):
    marks.append(
        int(input("Enter the marks of students to be added in the list: ")))
marks.sort()
print(marks)

# Write a program to sum a list with 4 numbers.

num = []
sum = 0
for i in range(4):
    num.append(int(input("Enter the number: ")))
    sum = sum + num[i]
print("The sum of all the Numbers is: ", sum)

# Write a program to count the number of zeroes in the following tuple

myTuple = (7, 0, 8, 0, 0, 9)
print(myTuple.count(0))
