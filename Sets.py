mySet = {1, 35, 67}

# Methods of Set

mySet.add(57)
mySet.add("1")
print(mySet)

print(len(mySet))

mySet.remove(35)
print(mySet)

print(mySet.pop())
print(mySet)

mySet.clear()
print(mySet)

# Union

mySet = {1, 8, 2, 3}
print(mySet.union({8, 11}))
print(mySet)

#  Intersection

mySet = {1, 8, 2, 3}
print(mySet.intersection({8, 11}))
