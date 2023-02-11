# printing and breaking the string/traversing

# var = "Hi My name is Rithik"
# print(var[3:-1])

# skip value of a string

# var = 'abcdefghijklmnopqrstuvwxyz'
# print(var[1:10])
# print(var[1:10:1])
# print(var[0:])
# print(var[:26])

# String Functions

# var = 'abcdefghijklmnopqrstuvwxyz'
# print(len(var))

# x = var.endswith('xyz')
# print(x)

# print(var.endswith('z'))
# print(var.startswith('abcd'))
# print(var.count('a'))

# Capitalize Function

# var = "my name is rithik"
# print(var.capitalize())

# print(var.find('rithik'))

# print(var.replace('rithik', 'agrawal'))

# Escape sequence characters

# var = "My \tname is\nRit\"hik"
# print(var)

# ==================================================

# var = input("Enter your name: ")
# print("Good Afternoon", var)
# print("Good Afternoon " + var)

#

# name = input("Enter the name: ")
# date = input("Enter the date: ")

# template = '''
# Dear <|name|>,
# you are selected
# <|date|>
# '''

# print(template.replace('<|name|>', name).replace("<|date|>", date))

# Detect double spaces in a String

# var = "My na  me is  hyina  bnhi aaa  "
# returns the index
# print(var.find("  "))

# returns -1 if not present
# print(var.find("Hiiiii"))

# Detect double spaces in a String

# var = "My na  me is  hyina  bnhi aaa  "

# print(var.replace("  ", " "))

#

var = "Dear Harry,\n\tThis Python Course is nice.\nThanks!"
print(var)
