# Python is a general-purpose, high-level programming language. It is the most popular language among developers and programmers as it can be used in Machine Learning, Web Development, Image Processing, etc.   

# 1. What is Python? List some popular applications of Python in the world of technology?
# Python is a widely-used general-purpose, high-level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. 
# It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code.
# It is used for:
# System Scripting
# Web Development
# Game Development
# Software Development
# Complex Mathematics

# 2. What are the benefits of using Python language as a tool in the present scenario?

# Object-Oriented Language
# High Level Language
# Dynamically Typed language
# Extensive support Libraries
# Presence of third-party modules
# Open source and community development
# Portable and Interactive
# Portable across Operating systems

# 3. Which sorting technique is used by sort() and sorted() functions of python?
# Python uses Tim Sort algorithm for sorting. It’s a stable sorting whose worst case is O(N log N). 
# It’s a hybrid sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data.

# 4. Differentiate between List and Tuple?
# Lists are Mutable datatype.
# Lists consume more memory
# The list is better for performing operations, such as insertion and deletion.
# Implication of iterations is Time-consuming

# Tuples are Immutable datatype.
# Tuple consume less memory as compared to the list
# Tuple data type is appropriate for accessing the elements
# Implication of iterations is comparatively Faster

# 5. How memory management is done in Python?
# Python uses its private heap space to manage the memory. Basically, all the objects and data structures are stored in the private heap space. 
# Even the programmer can not access this private space as the interpreter takes care of this space. Python also has an inbuilt garbage collector, 
# which recycles all the unused memory and frees the memory and makes it available to the heap space.

# 6. What is PEP 8?
# PEP 8 is a Python style guide. It is a document that provides the guidelines and best practices on how to write beautiful Python code. It promotes a very readable and eye-pleasing coding style.

# 7. Is Python a compiled language or an interpreted language?
# Actually, Python is a partially compiled language and partially interpreted language. 
# The compilation part is done first when we execute our code and this will generate byte code and internally this byte code gets converted by the python virtual machine(p.v.m) according to the underlying platform(machine+operating system).

# 8. How to delete a file using Python?
# os.remove()
# os.unlink()

# 9. What are Decorators?
# Decorators are a very powerful and useful tool in Python as they are the specific change that we make in Python syntax to alter functions easily.

# 10. What is the difference between Mutable datatype and Immutable datatype?
# Mutable data types can be edited i.e., they can change at runtime. Eg – List, Dictionary, etc.
# Immutable data types can not be edited i.e., they can not change at runtime. Eg – String, Tuple, etc.

# 11. What is the difference between Set and Dictionary?
# Set is an unordered collection of data type that is iterable, mutable, and has no duplicate elements.
# Dictionary in Python is an unordered collection of data values, used to store data values like a map.

# 12. How do you debug a Python program?
# By using this command we can debug a python program:
# $ python -m pdb python-script.py

# 13. What is Pickling and Unpickling?
# Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using the dump function, this process is called pickling. 
# While the process of retrieving original Python objects from the stored string representation is called unpickling.

# 14. How are arguments passed by value or by reference in Python?
# Everything in Python is an object and all variables hold references to the objects. The reference values are according to the functions; as a result, you cannot change the value of the references. However, you can change the objects if it is mutable.

# 15. What is List Comprehension? Give an Example.
# List comprehension is a syntax construction to ease the creation of a list based on existing iterable.
# my_list = [i for i in range(1, 10)]

# 16. What is Dictionary Comprehension? Give an Example
# Dictionary Comprehension is a syntax construction to ease the creation of a dictionary based on the existing iterable.
# my_dict = {i:3+i for i in range(1, 5)}
# print(my_dict)

# 17. Is Tuple Comprehension? If yes, how and if not why?
# (i for i in (1, 2, 3))
# Tuple comprehension is not possible in Python because it will end up in a generator, not a tuple comprehension.

# 18. What is namespace in Python?
# A namespace is a naming system used to make sure that names are unique to avoid naming conflicts.

# 19. What is a lambda function?
# A lambda function is an anonymous function. This function can have any number of parameters but, can have just one statement. 

# a = lambda x, y : x*y
# print(a(7, 16))

# 20. What is a pass in Python?
# Pass means performing no operation or in other words, it is a place holder in the compound statement, where there should be a blank left and nothing has to be written there.

# 21. What is the difference between xrange and range function?
# range() and xrange() are two functions that could be used to iterate a certain number of times in for loops in Python. In Python 3, there is no xrange, but the range function behaves like xrange in Python 2.

# range() – This returns a list of numbers created using range() function.
# xrange() – This function returns the generator object that can be used to display numbers only by looping. The only particular range is displayed on demand and hence called lazy evaluation.

# 22. What is difference between / and // in Python?
# // represents floor division whereas / represents precised division. For Example:
# 7//2 = 3
# 7/2 = 3.5

# 23. What is zip function?
# Python zip() function returns a zip object, which maps a similar index of multiple containers. It takes an iterable, converts into iterator and aggregates the elements based on iterables passed. It returns an iterator of tuples.

# 24. What is swapcase function in Python?
# It is a string’s function that converts all uppercase characters into lowercase and vice versa. It is used to alter the existing case of the string. This method creates a copy of the string which contains all the characters in the swap case. 

# 25. What are Iterators in Python?
# In Python, iterators are used to iterate a group of elements, containers like a list. Iterators are the collection of items, and it can be a list, tuple, or a dictionary. Python iterator implements __itr__ and the next() method to iterate the stored elements. 
# In Python, we generally use loops to iterate over the collections (list, tuple).

# 26. What are Generators in Python?
# In Python, the generator is a way that specifies how to implement iterators. It is a normal function except that it yields expression in the function. It does not implements __itr__ and next() method and reduces other overheads as well.
# If a function contains at least a yield statement, it becomes a generator. The yield keyword pauses the current execution by saving its states and then resumes from the same when required.

# 27. What are the new features added in Python 3.8 version?

# Positional Only parameter(/)
# Assignment Expression(:=)
# f-strings now support “=”
# reversed() works with a dictionary

# 28. What is monkey patching in Python?
# In Python, the term monkey patch only refers to dynamic modifications of a class or module at run-time.

# 29. Does Python supports multiple Inheritance?
# Python does support multiple inheritance, unlike Java. Multiple inheritance means that a class can be derived from more than one parent classes.

# 30. What is Polymorphism in Python?
# Polymorphism means the ability to take multiple forms. So, for instance, if the parent class has a method named ABC then the child class also can have a method with the same name ABC having its own parameters and variables. Python allows polymorphism.

# 31. Define encapsulation in Python?
# Encapsulation means binding the code and the data together. A Python class is an example of encapsulation.

# 32. How do you do data abstraction in Python?
# Data Abstraction is providing only the required details and hiding the implementation from the world. It can be achieved in Python by using interfaces and abstract classes.

# 33. Which databases are supported by Python?
# MySQL (Structured) and MongoDB (Unstructured) are the prominent databases that are supported natively in Python. Import the module and start using the functions to interact with the database.

# 34. How is Exceptional handling done in Python?
# There are 3 main keywords i.e. try, except, and finally which are used to catch exceptions and handle the recovering mechanism accordingly. Try is the block of a code which is monitored for errors. Except block gets executed when an error occurs.
# The beauty of the final block is to execute the code after trying for error. This block gets executed irrespective of whether an error occurred or not. Finally block is used to do the required cleanup activities of objects/variables.

# 35. What does ‘#’ symbol do in Python?
# ‘#’ is used to comment out everything that comes after on the line.

# 36. Write a code to display the current time?
# curr_time= time.localtime(time.time())
# print (“Current time is”, curr_time)

# 37. What is the difference between a shallow copy and deep copy?
# Shallow copy is used when a new instance type gets created and it keeps values that are copied whereas deep copy stores values that are already copied.
# A shallow copy has faster program execution whereas deep copy makes it slow.

# 38. What is PIP?
# PIP is an acronym for Python Installer Package which provides a seamless interface to install various Python modules. It is a command-line tool that can search for packages over the internet and install them without any user interaction.

# 39. What is __init__() in Python?
# Equivalent to constructors in OOP terminology, __init__ is a reserved method in Python classes. The __init__ method is called automatically whenever a new object is initiated. This method allocates memory to the new object as soon as it is created. 
# This method can also be used to initialize variables.

# 40. What is the maximum possible length of an identifier?
# Identifiers in Python can be of any length.






