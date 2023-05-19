# --------------- Python OOPs ---------------

# ----- Class -- 
""" A class is a blueprint or template that defines the structure and 
behavior of objects. It encapsulates data (attributes) and functions 
(methods) that operate on that data. Here's an example:
"""

# Example 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice", 25)
person1.say_hello()  # Output: Hello, my name is Alice and I am 25 years old.


"""
In the above example, we define a Person class with the __init__ method as the 
constructor, which initializes the name and age attributes. The say_hello method 
prints a greeting message using the object's attributes.

"""

# ------- Object/Instance ------------
"""An object is an instance of a class. It represents a particular 
entity based on the class definition. Multiple objects can be created 
from a single class. Here's an example:

"""

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.name)  # Output: Alice
print(person2.age)   # Output: 30

"""
In this example, person1 and person2 are objects of the Person 
class with different attribute values.

"""

# --------- Inheritance --------------
"""
Inheritance is a mechanism that allows a class to inherit attributes 
and methods from another class, known as the base class or superclass. 
It promotes code reuse and enables hierarchical relationships. Here's an example:

"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()  # Output: Woof!
cat.speak()  # Output: Meow!

"""
In this example, the Animal class serves as the base class, 
while the Dog and Cat classes inherit from it. The speak method 
is overridden in the derived classes to provide different behavior.

"""

# ---------- Polymorphism -----------
"""
Polymorphism allows objects of different classes to be treated as objects 
of a common base class. It enables flexibility and dynamic behavior. 
Here's an example using method overriding:

"""

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(shape.area())

"""
In this example, the Shape class serves as the base class with an area method. 
The Rectangle and Circle classes inherit from Shape and override the area method 
to provide their specific implementations. The list shapes contains instances of 
both classes, and calling the area method on each shape dynamically selects the 
appropriate implementation.

"""
# -------- Encapsulation ------------
"""
Encapsulation is the process of hiding internal details and providing a public 
interface to interact with objects. It helps in data protection and code organization.
 Here's an example using private attributes:

"""

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Private attribute
        self._balance = balance                # Private attribute

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self._balance

account = BankAccount("1234567890", 1000)
account.deposit(500)
print(account.get_balance())    # Output: 1500


"""
n this example, the BankAccount class has private attributes 
(_account_number and _balance) denoted by a single underscore prefix. 
These attributes are intended to be accessed only within the class. 
The public methods (deposit, withdraw, get_balance) provide a controlled 
interface for interacting with the object's data

"""
# -----------  Abstraction ----------------

"""
Abstraction is a concept in object-oriented programming that allows you to create 
abstract classes and methods. It focuses on providing a high-level, simplified 
interface to interact with objects, while hiding the underlying implementation details. 
Abstraction helps in creating modular and loosely coupled code. In Python, abstraction 
can be achieved through abstract base classes and abstract methods using the abc module.

"""

from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Concrete class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating objects
rectangle = Rectangle(4, 5)
circle = Circle(3)

# Calling abstract methods
print(rectangle.area())     # Output: 20
print(rectangle.perimeter())  # Output: 18.0
print(circle.area())        # Output: 28.26
print(circle.perimeter())   # Output: 18.84


"""
* In this example, we define an abstract base class Shape that inherits from the ABC class in the abc module. The Shape class has two abstract methods: area() and perimeter(). 
    These methods are declared with the @abstractmethod decorator, indicating that they must be implemented by any concrete class that inherits from Shape.

** The Rectangle and Circle classes are concrete classes that inherit from Shape and provide their own implementations of the abstract methods.

*** By defining abstract methods in the abstract base class, we enforce that any class inheriting from Shape must implement these methods. This allows us to work with 
        objects of different shapes (e.g., rectangles and circles) through a common interface (Shape), without worrying about their specific implementations.

****  Abstraction enables you to work with higher-level concepts and simplifies the interaction with objects by hiding the complexities of their internal workings.

"""