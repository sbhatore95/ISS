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

Exercise:

Write inside a file with your name on the first line and roll number on the second. Then
read inside the file to check if the name is palindrome or not. Do the same with the
roll number.
