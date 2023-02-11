a = 12
b = True
c = "This is a List"

myList = [a, b, c]

print(myList)
print(type(myList))
print(myList[2])
print(myList[0:3])
print(myList[0:300])

# List Functions/Methods

myList = [1, 8, 7, 2, 21, 15, 21]
myList.sort()  # Sorts the original list
myList.reverse()  # Reverses the original list
myList.append(9)  # Add 9 to the end of the original list
myList.insert(2, 9)  # Insert 9 at index 2
myList.pop()  # Removes an item from the end of the list
myList.pop(2)  # Removes an item from the given index from the list
myList.remove(21)  # Removes the first occurence of a  given item from the list
print(myList)
