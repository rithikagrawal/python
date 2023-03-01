# Create a class C-2D Vector and use it to create another class representing 3-D vector.

class Vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def printVector(self):
        print(f"{self.i}i + {self.j}j")


class Vector3D(Vector2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def printVector(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")


v2 = Vector2D(1, 5)
v2.printVector()
v3 = Vector3D(1, 5, 9)
v3.printVector()

# Create a class Pets from Animals and further create class Dog from Pets. Add a method bark to class Dog.


class Animals:
    def __init__(self) -> None:
        print("Animals >")


class Pets(Animals):
    def __init__(self) -> None:
        super().__init__()
        print("Pets >")


class Dog(Pets):
    def __init__(self) -> None:
        super().__init__()
        print("Dog >")

    def bark(self):
        print("Woof!")


dog = Dog()
dog.bark()

# Create a class Employee and add Salary and increment properties to it.
# Write a method salaryAfterIncrement method with a @property decorator with a setter which changes the value of increment based on the salary.


class Employee:
    def __init__(self, salary, increment) -> None:
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary * (1 + (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self):
        self.salary = self.salary * (1 + (self.increment/100))


sal = int(input("Enter Salary of Employee: "))
inc = int(input(f"Enter increment in % for Employee: "))
emp = Employee(sal, inc)
print(emp.salaryAfterIncrement)
emp.salaryAfterIncrement = 12300

# Write a class complex to represent complex numbers along with overloaded operators + and * which adds and multiplies them.


class Complex:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __add__(self, obj):
        return Complex(self.a+obj.a, self.b+obj.b)

    def __mul__(self, obj):
        return Complex(self.a * obj.a + ((self.b * obj.b)*(-1)), (self.a * obj.b) + (self.b * obj.a))


c1 = Complex(1, 4)
c2 = Complex(3, 9)
c3 = c1+c2
print(f"The Addition is {c3.a} + {c3.b}i")
c3 = c1*c2
print(f"The Multiplication is {c3.a} + {c3.b}i")


# Write a class vector reepresenting a vector of n dimension. Overload the + and * operator which calculates the sum and dot product of them.

class Vector:
    def __init__(self, l1) -> None:
        self.data = l1

    def __add__(self, obj):
        myList = []
        for i in range(len(obj.data)):
            myList.append(obj.data[i] + self.data[i])
        return Vector(myList)

    def __mul__(self, obj):
        dot = 0
        for i in range(len(obj.data)):
            dot += (obj.data[i]*self.data[i])
        return dot

    def __len__(self):
        return len(self.data)


v1 = Vector([1, 2, 3])
v2 = Vector([11, 12, 13])
v3 = v1+v2
print(f"The sum of two vectors is {v3.data}")

v4 = v1*v2  # v4 is a scalar
print(f"The dot product of two vectors is {v4}")

print(len(v3))


# Write __str__() method to print the vector as follows:
# 7i = 8j = 10k
# Assume vector of dimension 3 for this problem

class Vector:
    def __init__(self, i, j, k) -> None:
        self.i = i
        self.j = j
        self.k = k

    def __str__(self) -> str:
        return (f"{self.i}i +{self.j}j + {self.k}k")


v1 = Vector(7, 8, 10)
print(v1)
