# Class 02
## Object-oriented programming (OOP)
In object-oriented programming, concepts are modeled as classes and objects. An idea is defined using a class, and an instance of this class is called an object.

## Class
A Class is like an object constructor, or a "blueprint" for creating objects. Classes also have attributes and methods associated with them. Attributes are the characteristics of the class, while methods are functions that are part of the class.

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
```
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

## Attributes
A value associated with an object which is referenced by name using dotted expressions.
```python
    self.name = name
    self.age = age
```
## Methodes
 A function which is defined inside a class body. If called as an attribute of an instance of that class, the method will get the instance object as its first argument (which is usually called self).
 ```python
 class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
```
**Note:** The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

## Mutable and Immutable in Python 
An object whose internal state can be changed is mutable. On the other hand, immutable doesn’t allow any change in the object once it has been created.

### Mutable Definition
Mutable is when something is changeable or has the ability to change. In Python, ‘mutable’ is the ability of objects to change their values. These are often the objects that store a collection of data.

### Immutable Definition
Immutable is the when no change is possible over time. In Python, if the value of an object cannot be changed over time, then it is known as immutable. Once created, the value of these objects is permanent.

### List of Mutable and Immutable objects

#### Objects of built-in type that are mutable are:
* Lists
* Sets
* Dictionaries
* User-Defined Classes (It purely depends upon the user to define the characteristics) 

#### Objects of built-in type that are immutable are:
* Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
* Strings
* Tuples
* Frozen Sets
* User-Defined Classes (It purely depends upon the user to define the characteristics)
