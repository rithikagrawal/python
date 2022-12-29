oxford = {
    "gift": "Something willingly given to someone to appreciate",
    "this": "A keyword in C++",
    "youtube": "A video sharing platform",
    "instagram": "A picture sharing platform",
    "myList": [1, 3, 45]
}

# Methods for Dictionary
print(oxford.items())

for a, b in oxford.items():
    print(a, ":", b)

for key in oxford.keys():
    print(key)

# To add new Item
oxford.update({"rithik": "My Name"})
print(oxford)

# To update existing
oxford.update({"myList": [1, 1, 1, 1]})
print(oxford)

print(oxford['notPresent'])  # Throws error

print(oxford.get('notPresent'))  # Returns None
