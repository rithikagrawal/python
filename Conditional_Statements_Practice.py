# Write a program to print yes when the age entered by the user is greateer or equal to 18.

age = int(input("Please Enter the age: "))

if (age >= 18):
    print("Yes!!!")
else:
    print("No!!!")

#  Write a program to find greatest of 4 numbers entered by the user.

a = []
for i in range(4):
    a.append(int(input("Enter a Number: ")))

if (a[0] > a[1]):
    maxNum1 = a[0]
else:
    maxNum1 = a[1]

if (a[2] > a[3]):
    maxNum2 = a[2]
else:
    maxNum2 = a[3]

if (maxNum1 > maxNum2):
    maxNum = maxNum1
else:
    maxNum = maxNum2

print(maxNum, "is the largest among", a)

# Write a program to find out whether a student is pass or fail, if it rqeuires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

student = []
flag = 0
sumTotal = 0
for i in range(3):
    student.append(int(input("Enter the marks for student")))

for i in range(3):
    sumTotal = sumTotal + student[i]
    if ((student[i]/100)*100 >= 33):
        flag += 1
    else:
        print("Student is Failed!!, As he got less than '33%'")
        break

if (flag == 3 and ((sumTotal/300)*100) > 40):
    print("Student is Passed with", (sumTotal/300*100), "Percentage!")

# A spam comment is defined as a text containing following keywords: "make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

spamWords = ["make a lot of money", "buy now", "subscribe this", "click this"]

givenString = "This is a nice Stock. You need to click this  and buy now."

for word in spamWords:
    if (word in givenString):
        spam = word
    else:
        spam = False

if (spam):
    print("Spam word in given string is:", spam)
else:
    print("The given string is spam free")

# Write a program to find whether a given username contains less than 10 characters or not?

username = input("Enter your Username: ")

if (len(username) < 10):
    print("Less than 10 characters...")
else:
    print("More than 10 characters...")

# Write a program which finds out whether a given name is present in a list or not.

givenList = ["rithik", "ayush", "aniket", "then"]

inputText = input("Enter a name: ")

if inputText in givenList:
    print(inputText, "is present in the given list")
else:
    print(inputText, " is not present in given list")


# Write a program to calculate the grade of a student from his marks from the following scheme:

#           90-100 -> Ex
#           80-90 -> A
#           70-80 -> B
#           60-70 -> C
#           50-60 -> D
#            <50 -> F


grade = int(input("Enter the marks of the student to calculate the grades:"))

if (grade >= 90 and grade <= 100):
    print("The grade of student is Ex")
elif (grade >= 80 and grade < 90):
    print("The grade of student is A")
elif (grade >= 70 and grade < 80):
    print("The grade of student is B")
elif (grade >= 60 and grade < 70):
    print("The grade of student is C")
elif (grade >= 50 and grade < 60):
    print("The grade of student is D")
else:
    print("The grade of student is F")
