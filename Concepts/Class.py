# Sample Class
class Test:
    name = "Rithik"
    age = 22
    city = "JBP"

    def printObj(self):
        print(f"The name is {self.name}")


obj = Test()  # A basic object

print(obj.name)
print(obj.age)
print(obj.city)
obj.printObj()


# Create a class programmer for storing information of few programmers working at microsoft.

class Programmer:

    def __init__(self, name, language):
        self.name = name
        self.language = language


rithik = Programmer("Rithik", "Typescript")
ayush = Programmer("Ayush", "Python")
piyush = Programmer("Piyush", "Java")

print(rithik.name, rithik.language)
print(ayush.name, ayush.language)
print(piyush.name, piyush.language)

# Write a class calculator capable of finding square, cue and squareroot of a number.


class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"The square of {self.number} is: {self.number**2}")

    def cube(self):
        print(f"The cube of {self.number} is:  {self.number**3}")

    def squareRoot(self):
        print(
            f"The square root of {self.number} is: {self.number**(1/2)}")


num = float(input("Enter a number: "))
calculator = Calculator(num)
calculator.square()
calculator.cube()
calculator.squareRoot()

# Create a class with attribute a ; Create an object from it and set a directly using object a =0. Does this change the class attribute?


class AttributeTest():
    a = 10


obj = AttributeTest()
obj.a = 0
print(obj.a)
obj2 = AttributeTest()
print(obj2.a)

# Add a static method in problem 2 to greet the user with Hello.
# Write a class calculator capable of finding square, cue and squareroot of a number.


class Calculator:
    def __init__(self, number):
        self.number = number

    @staticmethod
    def hello():
        user = input("Please Enter your name: ")
        print(f"Hello {user}! Welcome to the Calculator Class.")

    def square(self):
        print(f"The square of {self.number} is: {self.number**2}")

    def cube(self):
        print(f"The cube of {self.number} is:  {self.number**3}")

    def squareRoot(self):
        print(
            f"The square root of {self.number} is: {self.number**(1/2)}")


num = float(input("Enter a number: "))
calculator = Calculator(num)
calculator.hello()
calculator.square()
calculator.cube()
calculator.squareRoot()

# Write a class Train which has methods to book a ticket, get status(no. of seats) and get Fare Information of trains running under Indian Railways.


class IndianRailways:
    def __init__(self) -> None:
        self.totalNumberOfSeats = 100
        self.fareForOneTicket = 80

    def bookTickets(self, numberOfSeats):
        availableSeats = self.getStatus()
        if (availableSeats >= numberOfSeats):
            self.getFareInfo(numberOfSeats)
            print("Are you sure? You want to confirm?")
            confirmation = input("Yes or No: ")
            if (confirmation == "Yes"):
                self.totalNumberOfSeats = self.totalNumberOfSeats-numberOfSeats
                print(f"The Boooking is confirmed for {numberOfSeats} seats.")
            else:
                print("Booking Cancelled!")
        elif (self.totalNumberOfSeats <= 0):
            print("Sorry! There are no available seats.")

    def getStatus(self):
        if (self.totalNumberOfSeats > 0):
            print(
                f"The total number of available seats are only {self.totalNumberOfSeats}.")
        else:
            print("Sorry! There are no available seats.")
        return self.totalNumberOfSeats

    def getFareInfo(self, numberOfSeats):
        print(
            f"The total fare for {numberOfSeats} seats is = {numberOfSeats*self.fareForOneTicket} $ ")


indianRailways = IndianRailways()
indianRailways.bookTickets(20)
indianRailways.getStatus()
indianRailways.getFareInfo(23)

# Can you change the self parameter inside a class to something else (say 'rithik'). Try changing self to 'slf' or "rithik" and see the effects.


class Demo:
    def __init__(rithik):
        rithik.num = 10


demo = Demo()
print(demo.num)
