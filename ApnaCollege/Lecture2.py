# String
str1 = "This is apna college's tutorial"
str2 = 'ApnaCollege'
str3 = """This is a string"""

# Escape sequence characters
"""
str4 = "This is a string. \nwe are creating it in python"
print(str4)

str5 = "This is a string. \twe are creating it in python"
print(str5)
"""

# Basic string operations
# 1. Concatenation
"""
first_name = "Shohel"
last_name = "Rana"
full_name = first_name + " " + last_name

print(full_name)
"""

# 2. Length of a string
"""
str4 = "This is a string."
length = len(str4)

print(length)
"""

# Indexing
"""
str = "Apna College" # 0 1 2 3 4 5 6 7 8 9 10 11
print(str[0]) # A
print(str[1]) # p
print(str[2]) # n
print(str[3]) # a
print(str[4]) # white space


# str[4] = "@"  # Error: string object does not support item assignment because strings are immutable
# print(str)
"""

# Slicing
"""
# Positive indexing
str = "Apna College" # 0 1 2 3 4 5 6 7 8 9 10 11
print(str[1:4]) # pna
print(str[5:12]) # College
print(str[5:len(str)]) # College
print(str[:4]) # Apna
print(str[5:]) # College

# Negative indexing
str = "Shohel Rana" # -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(str[-3:len(str)]) # ana
print(str[-3:]) # ana
print(str[-11:-5]) # Shohel
print(str[-4:]) # Rana
print(str[:-5]) # Shohel
"""

# String methods
str = "i am studying python from ApnaCollege from Youtube"
print(str.endswith("tube")) # True
print(str.endswith("app")) # False

print(str.capitalize()) # I am studying python from apnacollege from youtube
print(str) # Original string remains unchanged

print(str.replace("o", "a")) # i am studying pythan fram ApnaCallege fram Yautube
print(str.replace("python", "javascript")) # i am studying javascript from ApnaCollege from Youtube

print(str.find("o")) # 18
print(str.find("from")) #21
print(str.find("Q")) # -1 (not found)

print(str.count("from")) # 2
print(str.count("o")) # 5

