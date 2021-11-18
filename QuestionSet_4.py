# 1) What is Python?

# Python was created by Guido van Rossum, and released in 1991.
# It is a general-purpose computer programming language. 
# It is a high-level, object-oriented language which can run equally on different platforms such as Windows, Linux, UNIX, and Macintosh. 
# Its high-level built-in data structures, combined with dynamic typing and dynamic binding. 
# It is widely used in data science, machine learning and artificial intelligence domain.
# It is easy to learn and require less code to develop the applications.

# It is widely used for:

# Web development (server-side).
# Software development.
# Mathematics.
# System scripting.

# 2) Why Python?
# Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
# Python is compatible with different platforms like Windows, Mac, Linux, Raspberry Pi, etc.
# Python has a simple syntax as compared to other languages.
# Python allows a developer to write programs with fewer lines than some other programming languages.
# Python runs on an interpreter system, means that the code can be executed as soon as it is written. 
# It helps to provide a prototype very quickly.
# Python can be described as a procedural way, an object-orientated way or a functional way.
# The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

# 3) What are the applications of Python?
# Python is used in various software domains some application areas are given below.

# Web and Internet Development
# Games
# Scientific and computational applications
# Language development
# Image processing and graphic design applications
# Enterprise and business applications development
# Operating systems
# GUI based desktop applications
# Python provides various web frameworks to develop web applications. The popular python web frameworks are Django, Pyramid, Flask.
# Python's standard library supports for E-mail processing, FTP, IMAP, and other Internet protocols.
# Python's SciPy and NumPy helps in scientific and computational application development.
# Python's Tkinter library supports to create a desktop based GUI applications.

# 4) What are the advantages of Python?
# Python is (Interpreted language:It does not require prior compilation of code and executes instructions directly.)
# It is (Free and open source: It is an open-source project which is publicly available to reuse. It can be downloaded free of cost.)
# It is (Extensible: It is very flexible and extensible with any module.)
# Object-oriented: Python allows to implement the Object-Oriented concepts to build application solution.
# It has (Built-in data structure: Tuple, List, and Dictionary are useful integrated data structures provided by the language.)
# Readability
# High-Level Language
# Cross-platform
# Portable: Python programs can run on cross platforms without affecting its performance.

# 5) What is PEP 8?
# PEP 8 stands for Python Enhancement Proposal, it can be defined as a document that helps us to provide the guidelines on how to write the Python code. 
# It is basically a set of rules that specify how to format Python code for maximum readability. It was written by Guido van Rossum, Barry Warsaw and Nick Coghlan in 2001.

# 6) What do you mean by Python literals?
# Literals can be defined as a data which is given in a variable or constant. Python supports the following literals:
# String literals are formed by enclosing text in the single or double quotes. For example, string literals are string values.
# Example:

# # in single quotes  
# single = 'python'  
# # in double quotes  
# double = "python"  
# # multi-line String  
# multi = ''' python 
#      multi-line   
#      string '''   

# Numeric Literals:- Python supports three types of numeric literals integer, float and complex.

# # Integer literal    
# a = 19    
# #Float Literal    
# b = 62.3     
# #Complex Literal     
# x = 93.14j     

# Boolean Literals: are used to denote Boolean values. It contains either True or False.

# p = (1 == True)  
# q = (1 == False)  
# r = True + 3  
# s = False + 7  
    
# print("p is", p)  ---->True
# print("q is", q)  ---->False
# print("r:", r)    ---->4
# print("s:", s)    ---->7

# Special literals: Python contains one special literal, that is, 'None'. 
# This special literal is used for defining a null variable. 
# If 'None' is compared with anything else other than a 'None', it will return false.

# Example:
# word = None  
# print(word)  
# Output:
# None

# 7) Explain Python Functions?
# A function is a section of the program or a block of code that is written once and can be executed whenever required in the program. 
# A function is a block of self-contained statements which has a valid name, parameters list, and body. 
# Functions make programming more functional and modular to perform modular tasks. 
# Python provides several built-in functions to complete tasks and also allows a user to create new functions as well.

# There are three types of functions:

# Built-In Functions: copy(), len(), count() are the some built-in functions.
# User-defined Functions: Functions which are defined by a user known as user-defined functions.
# Anonymous functions: These functions are also known as lambda functions because they are not declared with the standard def keyword.
# Example: A general syntax of user defined function is given below.

# def function_name(parameters list):    
#     #--- statements---    
#     return a_value   
 
# 8) What is zip() function in Python?
# Python zip() function returns a zip object, which maps a similar index of multiple containers. 
# It takes an iterable, convert into iterator and aggregates the elements based on iterables passed. It returns an iterator of tuples.

# zip(iterator1, iterator2, iterator3 ...)    
# Parameters

# iterator1, iterator2, iterator3: These are iterator objects that are joined together.
# Return
# It returns an iterator from two or more iterators.
#  Eg.  a=("Rahul", "Rita", "Rohan")
#       b=("Jenny", "Harry", "Simran")
#       print(zip(a,b))  ---->(('Rahul'. 'Jenny'). ('Rita'. 'Harry'). ('Rohan'. 'Simran'))

# Note: If the given lists are of different lengths, zip stops generating tuples when the first list ends. It means two lists are having 3, and 5 lengths will create a 3-tuple.

# 9) What is Python's parameter passing mechanism?
# There are two parameters passing mechanism in Python:

# Pass by references
# Pass by value
# By default, all the parameters (arguments) are passed "by reference" to the functions. 
# Thus, if you change the value of the parameter within a function, the change is reflected in the calling function as well. 
# It indicates the original variable. 
# For example, if a variable is declared as a = 10, and passed to a function where it's value is modified to a = 20. Both the variables denote to the same value.

# The pass by value is that whenever we pass the arguments to the function only values pass to the function, no reference passes to the function. 
# It makes it immutable that means not changeable. Both variables hold the different values, and original value persists even after modifying in the function.
# Python has a default argument concept which helps to call a method using an arbitrary number of arguments.

# 10) How to overload constructors or methods in Python?
# Python's constructor: _init__ () is the first method of a class. 
# Whenever we try to instantiate an object __init__() is automatically invoked by python to initialize members of an object. 
# We can't overload constructors or methods in Python. It shows an error if we try to overload.

# class student:    
#     def __init__(self, name):    
#         self.name = name    
#     def __init__(self, name, email):    
#         self.name = name    
#         self.email = email    
         
# # This line will generate an error    
# #st = student("rahul")    
    
# # This line will call the second constructor    
# st = student("Rahul", "rahul@gmail.com")    
# print("Name: ", st.name)       ----># Name:  Rahul
# print("Email id: ", st.email)  ----># Email id:  rahul@gmail.com

# 11) What is the difference between remove() function and del statement?
# The user can use the remove() function to delete a specific object in the list.
# list_1 = [ 3, 5, 7, 9, 3 ]   
# print(list_1)  
# list_1.remove(3)   
# print("After removal: ", list_1)  
# Output: [3, 5, 7, 9, 3]
# After removal: [5, 7, 9, 3]

# If you want to delete an object at a specific location (index) in the list, you can either use del or pop.
# list_1 = [ 3, 5, 7, 3, 9, 3 ]   
# print(list_1)  
# del list_1[2]  
# print("After deleting: ", list_1)  
# Output:[3, 5, 7, 3, 9, 3]
# After deleting: [3, 5, 3, 9, 3]

# Note: You don't need to import any extra module to use these functions for removing an element from the list.
# We cannot use these methods with a tuple because the tuple is different from the list.

# 12) What is swapcase() function in the Python?
# It is a string's function which converts all uppercase characters into lowercase and vice versa. 
# It is used to alter the existing case of the string. This method creates a copy of the string which contains all the characters in the swap case. 
# If the string is in lowercase, it generates a small case string and vice versa. It automatically ignores all the non-alphabetic characters. See an example below.

# string = "IT IS IN LOWERCASE."  
# print(string.swapcase())  
# string = "it is in uppercase."  
# print(string.swapcase())  
# Output:
# it is in lowercase. 
# IT IS IN UPPERCASE. 

# 13) How to remove whitespaces from a string in Python?
# To remove the whitespaces and trailing spaces from the string, Python providies strip([str]) built-in function. 
# This function returns a copy of the string after removing whitespaces if present. Otherwise returns original string.

# Example:

# string = "  python  "  
# string2 = "    python       "  
# string3 = "       python"  
# print(string)  
# print(string2)  
# print(string3)  
# print("After stripping all have placed in a sequence:")  
# print(string.strip())  
# print(string2.strip())  
# print(string3.strip())  
# Output:
# python
#     python       
#        python
# After stripping all have placed in a sequence:
# python
# python
# python

# 14) How to remove leading whitespaces from a string in the Python?
# To remove leading characters from a string, we can use lstrip() function. 
# It is Python string function which takes an optional char type parameter. 
# If a parameter is provided, it removes the character. Otherwise, it removes all the leading spaces from the string.

# Example:
# string = "  python "   
# string2 = "    python       "  
# print(string)  
# print(string2)  
# print("After stripping all leading whitespaces:")  
# print(string.lstrip())  
# print(string2.lstrip())  
# Output:

# python 
#     python        
# After stripping all leading whitespaces:
# python 
# python

# 15) Why do we use join() function in Python?
# The join() is defined as a string method which returns a string value. 
# It is concatenated with the elements of an iterable. 
# It provides a flexible way to concatenate the strings.

# str = "Rohit"  
# str2 = "ab"    
# str2 = str.join(str2)       
# print(str2)  
# Output:aRohitb

# 16) Give an example of shuffle() method?
# This method shuffles the given string or an array. It randomizes the items in the array. 
# This method is present in the random module. So, we need to import it and then we can call the function. 
# It shuffles elements each time when the function calls and produces different output.
 
# import random   
# sample_list1 = ['Z', 'Y', 'X', 'W', 'V', 'U']  
# print("Original LIST1: ")  
# print(sample_list1)    
# random.shuffle(sample_list1)  
# print("\nAfter the first shuffle of LIST1: ")  
# print(sample_list1)  
# random.shuffle(sample_list1)  
# print("\nAfter the second shuffle of LIST1: ")  
# print(sample_list1)  
# Output:

# Original LIST1: 
# ['Z', 'Y', 'X', 'W', 'V', 'U']

# After the first shuffle of LIST1: 
# ['V', 'U', 'W', 'X', 'Y', 'Z']

# After the second shuffle of LIST1: 
# ['Z', 'Y', 'X', 'U', 'V', 'W']

# 17) What is the use of break statement?
# The break statement is used to terminate the execution of the current loop. 
# Break always breaks the current execution and transfer control to outside the current block. 
# If the block is in a loop, it exits from the loop, and if the break is in a nested loop, it exits from the innermost loop.

# list_1 = ['X', 'Y', 'Z']  
# list_2 = [11, 22, 33]  
# for i in list_1:  
#     for j in list_2:  
#         print(i, j)  
#         if i == 'Y' and j == 33:  
#             print('BREAK')  
#             break  
#     else:  
#         continue  
#     break  
# Output:
# X 11
# X 22
# X 33
# Y 11
# Y 22
# Y 33
# BREAK

# 18) What is tuple in Python?
# A tuple is a built-in data collection type. It allows us to store values in a sequence. 
# It is immutable, so no change is reflected in the original data. It uses () brackets rather than [] square brackets to create a tuple. 
# We cannot remove any element but can find in the tuple. We can use indexing to get elements. 
# It also allows traversing elements in reverse order by using negative indexing. 
# Tuple supports various methods like max(), sum(), sorted(), Len() etc.

# Example: 
# tup = (29,14,36,28)  
# print(tup)  
# print(tup[3])  
# Output:

# (29, 14, 36, 28)
# 28

# It is immutable. So updating tuple will lead to an error.
 
# 19) Which are the file related libraries/modules in Python?
# The Python provides libraries/modules that enable you to manipulate text files and binary files on the file system. 
# It helps to create files, update their contents, copy, and delete files. The libraries are os, os.path, and shutil.
# os and os.path - modules include a function for accessing the filesystem
# while shutil - module enables you to copy and delete the files.

# 20) What are the different file processing modes supported by Python?
# Python provides four modes to open files. The read-only (r), write-only (w), read-write (rw) and append mode (a). 
# 1.Read-only mode (r): Open a file for reading. It is the default mode.
# 2.Write-only mode (w): Open a file for writing. If the file contains data, data would be lost. Other a new file is created.
# 3.Read-Write mode (rw): Open a file for reading, write mode. It means updating mode.
# 4.Append mode (a): Open for writing, append to the end of the file, if the file exists.
