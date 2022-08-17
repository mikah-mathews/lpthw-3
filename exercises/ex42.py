# Animal is-a object
class Animal(object)
  Pass

class Dog(animal):
  # Dog is-a object
  def __init__(self, name):
    # Dog has-a name of some kind
    self.name = name

class Cat(animal):
  # Cat is-a object
  def __init__(self, name):
  # Cat has-a name of some kind
    self.name = name

# Person is an object
class Person(object):
  def __init__(self, name):
    # person has a name of some kind
    self.name = name
    # person has a pet of some kind
    self.pet = None

# Employee is-a object that references the person object
class Employee(person):
  def __init__(self, name, salary):
    # this means that it inherits/'has-a' the properties of person, but currently is only grabbing the data for 'name' from it
    super(Employee, self).__init__(name)
    self.salary = salary

# This is-a object of Fish
class Fish(object):
  Pass

# This is-a object of Salmon
class Salmon(Fish):
  Pass

# This is-a object of Halibut
class Halibut(Fish):
  Pass

# Rover is-a dog
rover = Dog("Rover")

# Satan is-a cat
satan = Cat("Satan")

# Mary is-a Person
mary = Person("Mary")

# Mary has-a cat
mary.pet = satan

# Frank is-a employee
frank = Employee("Frank", 120000)

# Frank has-a pet
frank.pet = rover

# Flipper is-a fish
flipper = Fish()

# Crouse is-a Salmon
crouse = Salmon()

# Harry is-a Halibut
harry = Halibut()