#  Write a program to create a dictionary of Hindi words with values as their english translation. Provide user with an option to look it up.

hindiToEnglish = {
    "lakdi": "wood",
    "kursi": "chair",
    "mazaak": "joke",
    "chaku": "knife",
    "utay": "there"
}

key = input("Enter the word to translate: ")

if (hindiToEnglish.get(key) == None):
    print("There is no translation available for", key,
          "as of now.\nYou can comeback later and check again.\nThank You!")
else:
    print("The transalation of", key, "in hindi is",
          hindiToEnglish.get(key) + ".")

print(hindiToEnglish[key])

# Write a program to input eight numbers from the user and display all the unique numbers(once).

uniqueSet = set()
for i in range(8):
    uniqueSet.add(input("Enter the number to add: "))
print(uniqueSet)

# Can we have a set with 18(int) and "18"(str) as a value in it

testSet = set()
for i in range(2):
    if (i == 0):
        testSet.add(input("Enter an item to be added in set: "))
    else:
        testSet.add(int(input("Enter a number to be added in set: ")))
print("Your Set is: ", testSet)

# What will be the legth of following set S

s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))  # ans: 2

# s={}, What is the type of s?

s = {}  # ans: dict
print(type(s))

# Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as their names. Assume that the names are unique.

friends = {}
for i in range(4):
    friends.update({input("Enter your name: "): input(
        "Enter your favourite language: ")})
print(friends)

# If names of two friends are same, what will happen in case above
# Answer is the dictionary or the update will override the language for the first friend.

friends = {}
for i in range(4):
    friends.update({input("Enter your name: "): input(
        "Enter your favourite language: ")})
print(friends)

# If languages of two friends are same, what will happen in case above
# Answer is the dictionary will accept it and both the friends will have same languages.

friends = {}
for i in range(4):
    friends.update({input("Enter your name: "): input(
        "Enter your favourite language: ")})
print(friends)

# Can you change the values inside a list which is converted in set below.
# exampleSet = {8, 7, 12, "Harry", [1, 2]}
# Answer is no we cannot update the value of set, because sets are unhashable that is unaccessible. In other words you can't access the value of set.
