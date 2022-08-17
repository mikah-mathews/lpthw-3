# Animal is-a object
class Animal(object)
  Pass

class Dog(animal):
  def __init__(self, name):
    self.name = name

class Cat(animal):
  def __init__(self, name):
    self.name = name

class Person(object):
  def __init__(self, name):
    self.name = name
    self.pet = None

class Employee(person):
  def __init__(self, name, salary):
    super(Employee, self).__init__(name)
    self.salary = salary

class Fish(object):
  Pass

class Salmon(Fish):
  Pass

class Halibut(Fish):
  Pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()