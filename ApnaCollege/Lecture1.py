# First Program
"""
print("Hello World")
print("My name is", "Shohel Rana")
"""

# Variables
"""
name = "Shohel Rana"
age = 30
isStudent = True

print("I am", name, "and i am", age, "years old.")
"""

# Data Types
"""
age = 30                # Integer
height = 5.9            # Float
name = "Shohel Rana"    # String
isStudent = True        # Boolean
bloodGroup = None       # NoneType

print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(name))       # <class 'str'>
print(type(isStudent))  # <class 'bool'>
print(type(bloodGroup)) # <class 'NoneType'>
"""

# Print Sum
"""
a = 10
b = 22.57
c = a + b

print(c)
"""

# Type of Operators
# Arithmetic Operators (+, -, *, /, %, **)
"""
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
"""

# Assignment Operators (=, +=, -=, *=, /=, %=, **=)
"""
num = 10
# num += 3    # num = num + 3
# num -= 3    # num = num - 3
# num *= 3    # num = num * 3
# num /= 3    # num = num / 3
# num %= 3    # num = num % 3
num **= 3   # num = num ** 3

print(num) 
"""

# Relational / Comparison Operators (==, !=, >, <, >=, <=)
"""
a = 10
b = 3

print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(a < b)    # False
print(a >= b)   # True
print(a <= b)   # False
"""

# Logical Operators (not, and, or)
"""
a = 10
b = 3

print(not (a > b))          # False => It's negate the value True <=> False
print((a > b) and (b < a))  # True => Every condition should be true
print((a > b) or (a < b))   # True => Only one conditon should be true
"""

# Type Conversion (Autometic conversion by Python interpretor)
"""
a = 2
b = 4.25
sum = a + b # 2.0 + 4.25 => 6.25

print(sum)

c = "5"
d = 3.53
print(c + d) # TypeError: can only concatenate str (not "float") to str
"""

# Type Casting (Manual conversion by user)
"""
a = int("2")
b = float(4)
c = 3.25
sum1 = a + b
sum2 = b + c

print(type(a))
print(sum1)

print(type(b))
print(sum2)
"""

# Input statement
"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Welcome", name)
print("age = ", age)
print("marks = ", marks)
print("Hello", name, "your age is", age, "and your marks are", marks)
"""

# Practice
# 1.  Write a program to take two numbers as input and print their sum.
"""
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
sum = first_number + second_number

print(first_number, "+", second_number, "=", sum)
"""

# 2. Write a program to input side of a square and print its area.
"""
side = float(input("Enter side of square: "))
area = side * side

print("Area of square is", area)
"""

# 3. Write a program to input 2 floating point numbers and print their average.
"""
float1 = float(input("Enter first floating point number: "))
float2 = float(input("Enter second floating point number: "))

average = (float1 + float2) / 2

print("Average of", float1, "and", float2, "is", average)
"""

# 4. Write a program to input 2 integer numbers a and b. Print True if a is greater than or equal to b, otherwise print False.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a >= b)