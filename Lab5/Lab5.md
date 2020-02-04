# Lab 5 : Python basics

## PEP8 standards 

[https://www.python.org/dev/peps/pep-0008/]

Read the link above to gain more insight into this. Some examples:
### Code Layout
1. Indentation

Use 4 spaces per indentation level. Spaces are the preferred indentation method.

2. Maximum Line Length

Limit all lines to a maximum of 79 characters.

### Comments

Comments that contradict the code are worse than no comments. Always make a
priority of keeping the comments up-to-date when the code changes!

## Functions

***Example:***

function to return sum of all natural numbers till num.

```python
def sumTillNum(num):
        sum = 0
        i = 1
        while(i != num+1):
                sum = sum + i
                i = i+1
        return sumi
```

## Lists, range, tuples

***Example:***

A function that takes a string as an argument and returns a list containing
the number of occurences of each character. (Assume string has only lowercase
alphabets.)

```python
def countOccurences(s):
        ans = [0]*26
        for i in range(0, len(s)):
                ans[ord(s[i]) - ord('a')] = ans[ord(s[i]) - ord('a')] + 1
        return ans
```

A tuple is a sequence of immutable Python objects. Some points to note:

1. Removing individual tuple elements is not possible.

Advantages of tuple over list:
1. Iteration in a tuple is faster as compared to lists since tuples in Python are immutable.
2. Tuples are generally used for different Python Data Types; whereas, lists are used for similar data types.
3. Whenever, we need to make sure that the data remains unchanged and write protected, Python tuple is the best option.

***Exercise***

1. Write a function that takes an argument N and returns a tuple containing average and sum of first N primes.
2. Given a list of strings as argument, return the number of strings that are palindrome.

 
## Exceptions

[https://docs.python.org/3/tutorial/errors.html]

```python
def this_fails():
        x = 1/0
try:
        this_fails()
except ZeroDivisionError as err:
        print('Handling run-time error:', err)
```

## Reading and writing file

Read example:

```python
f = open("filename", "r")
line = f.readline()
while line != "":
        print line
        line = f.readline()
f.close()
```

Write example:

```python
f = open("out.txt", "w")
f.write("Hey !!")
f.close()
```

***Exercise:***

Write inside a file with your name on the first line and roll number on the second. Then
read inside the file to check if the name is palindrome or not. Do the same with the
roll number.

## OOPS

Resource link: 
1. [https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-1-class-and-its-members/]
2. [https://www.programiz.com/python-programming/object-oriented-programming]

### Class and instance variable

Class example:

```python
class Test: 
	def foo(self): 
		print("Hello") 

# Driver code 
obj = Test() 
obj.fun() 
```

The __init__ method:

```python
class Karizma: 

	# init method or constructor 
	def __init__(self, model): 
		self.model = model 

	# Sample Method 
	def printModelName(self): 
		print(self.model) 

p = Karizma('ZMR') 
p.printModelName() 
```

Instance and class variable

```python
# Class for Computer Science Student 
class CSStudent: 

	# Class Variable 
	stream = 'cse'			

	# The init method or constructor 
	def __init__(self, roll): 
	
		# Instance Variable	 
		self.roll = roll	 

# Objects of CSStudent class 
a = CSStudent(101) 
b = CSStudent(102) 

print(a.stream) # prints "cse" 
print(b.stream) # prints "cse" 
print(a.roll) # prints 101 

# Class variables can be accessed using class 
# name also 
print(CSStudent.stream) # prints "cse"	 
```

An example:

```python
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))
```

### Inheritance

Inheritance is a way of creating new class for using details of existing class without
modifying it. The newly formed class is a derived class (or child class). Similarly, the 
existing class is a base class (or parent class).

```python
# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
```

```
Bird is ready
Penguin is ready
Penguin
Swim faster
Run faster
```

### Encapsulation

Using OOP in Python, we can restrict access to methods and variables. This prevent data
from direct modification which is called encapsulation. In Python, we denote private attribute
using underscore as prefix i.e single “ _ “ or double “ __“.

```python
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
```

### Polymorphism

Polymorphism is an ability (in OOP) to use common interface for multiple form (data types).

Suppose, we need to color a shape, there are multiple shape option (rectangle, square, circle). However we could use same method to color any shape. This concept is called Polymorphism.

```python
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
```
