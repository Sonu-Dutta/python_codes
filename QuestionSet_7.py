# Introduction to Python:
# Python was developed by Guido van Rossum and was released first on February 20, 1991. It is one of the most widely-used and loved programming languages and is interpreted in nature thereby providing flexibility of incorporating dynamic semantics. 
# It is also a free and open-source language with very simple and clean syntax. This makes it developers easy to learn python. Python also supports object-oriented programming and is most commonly used to perform general-purpose programming. 
# Due to its simplistic nature and the ability to achieve multiple functionalities in fewer lines of code, python’s popularity is growing tremendously. Python is also used in Machine Learning, Artificial Intelligence, Web Development, Web Scraping, 
# and various other domains due to its ability to support powerful computations using powerful libraries. Due to this, there is a huge demand for python developers in India and across the world. 
# Companies are willing to offer amazing perks and benefits to these developers. 

# 1. What is Python?
# Python is a high-level, interpreted, general-purpose programming language. Being a general-purpose language, it can be used to build almost any type of application with the right tools/libraries. 
# Additionally, python supports objects, modules, threads, exception-handling, and automatic memory management which help in modeling real-world problems and building applications to solve these problems.

# 2. What are the benefits of using Python?
# Python is a general-purpose programming language (it can be used for a wide variety of development task) that has a simple, easy-to-learn syntax that emphasizes readability and therefore reduces the cost of program maintenance. 
# Moreover, the language is capable of scripting, is completely open-source, and supports third-party packages encouraging modularity and code reuse.
# Its high-level data structures, combined with dynamic typing and dynamic binding, attract a huge community of developers for Rapid Application Development and deployment.

# 3. What is a dynamically typed language?
# Before we understand a dynamically typed language, we should learn about what typing is. Typing refers to type-checking in programming languages. 
# In a strongly-typed language, such as Python, "1" + 2 will result in a type error since these languages don't allow for "type-coercion" (implicit conversion of data types). 
# On the other hand, a weakly-typed language, such as Javascript, will simply output "12" as result.

# Type-checking can be done at two stages -

# Static - Data Types are checked before execution.
# Dynamic - Data Types are checked during execution.
# Python is an interpreted language, executes each statement line by line and thus type-checking is done on the fly, during execution. Hence, Python is a Dynamically Typed Language.

# 4. What is an Interpreted language?
# An Interpreted language executes its statements line by line. Languages such as Python, Javascript, R, PHP, and Ruby are prime examples of Interpreted languages. 
# Programs written in an interpreted language runs directly from the source code, with no intermediary compilation step.

# 5. What is PEP 8 and why is it important?
# PEP stands for Python Enhancement Proposal. A PEP is an official design document providing information to the Python community, or describing a new feature for Python or its processes. 
# PEP 8 is especially important since it documents the style guidelines for Python Code. Apparently contributing to the Python open-source community requires you to follow these style guidelines sincerely and strictly.

# 6. What is Scope in Python?
# Every object in Python functions within a scope. A scope is a block of code where an object in Python remains relevant. Namespaces uniquely identify all the objects inside a program. 
# However, these namespaces also have a scope defined for them where you could use their objects without any prefix. A few examples of scope created during code execution in Python are as follows:

# A local scope refers to the local objects available in the current function.
# A global scope refers to the objects available throughout the code execution since their inception.
# A module-level scope refers to the global objects of the current module accessible in the program.
# An outermost scope refers to all the built-in names callable in the program. The objects in this scope are searched last to find the name referenced.
# ***Local scope objects can be synced with global scope objects using keywords such as global.***

# 7. What are lists and tuples? What is the key difference between the two?
# Lists and Tuples are both sequence data types that can store a collection of objects in Python. The objects stored in both sequences can have different data types. 
# Lists are represented with square brackets [], while tuples are represented with parantheses ().
# The key difference between the two is that while lists are mutable, tuples on the other hand are immutable objects. 
# This means that lists can be modified, appended or sliced on the go but tuples remain constant and cannot be modified in any manner. 

# tup = ('Hello', 65, 0.897)
# lst = ['Hello', 65, 0.897]
# print(tup[0])     # output => 'Hello'
# print(lst[0])     # output => 'Hello'
# tup[0] = 'Hi'    # modifying tuple => throws an error
# lst[0] = 'Hi'    # modifying list => list modified
# print(tup[0])     # output => 'Hello'
# print(lst[0])     # output => 'Hi'

# 8. What are the common built-in data types in Python?
# There are several built-in data types in Python. Although, Python doesn't require data types to be defined explicitly during variable declarations type errors are likely to occur 
# if the knowledge of data types and their compatibility with each other are neglected. Python provides type() and isinstance() functions to check the type of these variables. These data types can be grouped into the following categories-

# None Type:
# None keyword represents the null values in Python. Boolean equality operation can be performed using these NoneType objects.
# NoneType	Represents the NULL values in Python.

# Numeric Types:
# There are three distinct numeric types - integers, floating-point numbers, and complex numbers. Additionally, booleans are a sub-type of integers.
# int: Stores integer literals including hex, octal and binary numbers as integers
# float: Stores literals containing decimal values and/or exponent signs as floating-point numbers
# complex: Stores complex numbers in the form (A + Bj) and has attributes: real and imag
# bool:	Stores boolean value (True or False).

# Sequence Types:
# According to Python Docs, there are three basic Sequence Types - lists, tuples, and range objects. 
# Sequence types have the in and not in operators defined for their traversing their elements. These operators share the same priority as the comparison operations.
# list: Mutable sequence used to store collection of items.
# tuple: Immutable sequence used to store collection of items.
# range: Represents an immutable sequence of numbers generated during execution.
# str: Immutable sequence of Unicode code points to store textual data.

# Mapping Types:
# A mapping object can map hashable values(remains the same during its lifetime) to random objects in Python. Mappings objects are mutable and there is currently only one standard mapping type, the dictionary.
# dict	Stores comma-separated list of (key: value) pairs
# Set Types:
# Currently, Python has two built-in set types - set and frozenset. set type is mutable and supports methods like add() and remove(). frozenset type is immutable and can't be modified after creation.
# set: Mutable unordered collection of distinct hashable objects.
# frozenset: Immutable collection of distinct hashable objects.
# Note: set is mutable and thus cannot be used as key for a dictionary. On the other hand, frozenset is immutable and thus, hashable, and can be used as a dictionary key or as an element of another set.

# Modules:
# Module is an additional built-in type supported by the Python Interpreter. It supports one special operation, i.e., attribute access: mymod.myobj, where mymod is a module and myobj references a name defined in m's symbol table. 
# The module's symbol table resides in a very special attribute of the module __dict__, but direct assignment to this module is neither possible nor recommended.

# Callable Types:
# Callable types are the types to which function call can be applied. They can be user-defined functions, instance methods, generator functions, and some other built-in functions, methods and classes.
# Refer to the documentation at docs.python.org for a detailed view of the callable types.

# 9. What is pass in Python?
# The pass keyword represents a null operation in Python. It is generally used for the purpose of filling up empty blocks of code which may execute during runtime but has yet to be written. 
# Without the pass statement in the following code, we may run into some errors during code execution.

# def myFun():
#    # do nothing
#    pass
# myFun()    # nothing happens

# ## Without the pass keyword
# # IndentationError: expected an indented block

# 10. What are modules and packages in Python?
# Python packages and Python modules are two mechanisms that allow for modular programming in Python. Modularizing has several advantages -

# Simplicity
# Maintainability 
# Reusability
# Scoping
# Modules, in general, are simply Python files with a .py extension and can have a set of functions, classes, or variables defined and implemented. 
# They can be imported and initialized once using the import statement. If partial functionality is needed, import the requisite classes or functions using from foo import bar.

# Packages allow for hierarchial structuring of the module namespace using dot notation. As, modules help avoid clashes between global variable names, in a similar manner, packages help avoid clashes between module names.
# Creating a package is easy since it makes use of the system's inherent file structure. So just stuff the modules into a folder and there you have it, the folder name as the package name. 
# Importing a module or its contents from this package requires the package name as prefix to the module name joined by a dot.

# 11. What are global, protected and private attributes in Python?
# Global variables are public variables that are defined in the global scope. To use the variable in the global scope inside a function, we use the global keyword.
# Protected attributes are attributes defined with an underscore prefixed to their identifier eg. _value. They can still be accessed and modified from outside the class they are defined in but a responsible developer should refrain from doing so.
# Private attributes are attributes with double underscore prefixed to their identifier eg. __value. They cannot be accessed or modified from the outside directly and will result in an AttributeError if such an attempt is made.

# 12. What is self in Python?
# Self is a keyword in Python used to define an instance of an object of a class. In Python, it is explicitly used as the first parameter, unlike in Java where it is optional. It helps in distinguishing between the methods and attributes of a class from its local variables.

# 13. What is __init__?
# __init__ is a contructor method in Python and is automatically called to allocate memory when a new object/instance is created. All classes have a __init__ method associated with them. It helps in distinguishing methods and attributes of a class from local variables.

# class Student:
#    def __init__(self, fname, lname, age):
#        self.firstname = fname
#        self.lastname = lname
#        self.age = age
# s1 = Student("Sandhya", "Dutta", "20")

# 14. What is break, continue and pass in Python?
# Break	The break statement terminates the loop immediately and the control flows to the statement after the body of the loop.
# Continue	The continue statement terminates the current iteration of the statement, skips the rest of the code in the current iteration and the control flows to the next iteration of the loop.
# The pass keyword in Python is generally used to fill up empty blocks and is similar to an empty statement represented by a semi-colon in languages such as Java, C++, Javascript, etc.
# num = [6, 7, 2, 5, 2, 8, 1, 0, 3, 9]
# for p in num:
#    pass
#    if (p == 0):
#         current = p
#         break
#    elif (p % 2 == 0):
#        continue
#    print(p)    # output =>  7 5 1
# print(current)    # output => 0

# 15. What are unit tests in Python?
# Unit test is a unit testing framework of Python.
# Unit testing means testing different components of software separately. Imagine a scenario, you are building software that uses three components namely A, B, and C. 
# Now, suppose your software breaks at a point time. How will you find which component was responsible for breaking the software? 
# Maybe it was component A that failed, which in turn failed component B, and this actually failed the software. There can be many such combinations.
# This is why it is necessary to test each and every component properly so that we know which component might be highly responsible for the failure of the software.

# 16. What is docstring in Python?
# Documentation string or docstring is a multiline string used to document a specific code segment.
# The docstring should describe what the function or method does.

# 17. What is slicing in Python?
# As the name suggests, ‘slicing’ is taking parts of.
# Syntax for slicing is [start : stop : step]
# start is the starting index from where to slice a list or tuple
# stop is the ending index or where to sop.
# step is the number of steps to jump.
# Default value for start is 0, stop is number of items, step is 1.
# Slicing can be done on strings, arrays, lists, and tuples.

# numb = [11, 22, 33, 34, 55, 66]
# print(numb[1 : : 2])  #output : [22, 44, 66]

# 18. Explain how can you make a Python Script executable on Unix?
# Script file must begin with #!/usr/bin/env python

# 19. What is the difference between Python Arrays and lists?
# Arrays in python can only contain elements of same data types i.e., data type of array should be homogeneous. It is a thin wrapper around C language arrays and consumes far less memory than lists.
# Lists in python can contain elements of different data types i.e., data type of lists can be heterogeneous. It has the disadvantage of consuming large memory.
import array
a = array.array('i', [1, 2, 3])
for i in a:
    print(i, end=' ')    #OUTPUT: 1 2 3
# a = array.array('i', [1, 2, 'hello'])    #OUTPUT: TypeError: an integer is required (got type str)
a = [4, 5, 'hello']
for i in a:
   print(i, end=' ')    #OUTPUT: 1 2 hello

# 20. How is memory managed in Python?
# Memory management in Python is handled by the Python Memory Manager. The memory allocated by the manager is in form of a private heap space dedicated to Python. 
# All Python objects are stored in this heap and being private, it is inaccessible to the programmer. Though, python does provide some core API functions to work upon the private heap space.
# Additionally, Python has an in-built garbage collection to recycle the unused memory for the private heap space.