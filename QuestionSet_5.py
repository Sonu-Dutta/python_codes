# 1) What is an operator in Python?
# An operator is a particular symbol which is used on some values and produces an output as a result. 
# An operator works on operands. Operands are numeric literals or variables which hold some values. 
# Operators can be unary, binary or ternary. An operator which requires a single operand known as a unary operator, 
# which require two operands known as a binary operator and which require three operands is called ternary operator.

# Example:
# # Unary Operator
# A = 12  
# B = -(A)  
# print (B)  
# # Binary Operator  
# A = 12  
# B = 13  
# print (A + B)  
# print (B * A)  
# #Ternary Operator  
# A = 12  
# B = 13  
# min = A if A < B else B     
# print(min)  
# Output:
# # Unary Operator
# -12
# # Binary Operator
# 25
# 156
# # Ternary Operator
# 12

# 2) What are the different types of operators in Python?
# Python uses a rich set of operators to perform a variety of operations. 
# Some individual operators like membership and identity operators are not so familiar but allow to perform operations.

# Arithmetic Operators
# Relational Operators
# Assignment Operators
# Logical Operators
# Membership Operators
# Identity Operators
# Bitwise Operators

# Example: 
# print(32+13)  ---->45
# print(42-23)  ---->19 
# print(2*23)   ---->46 
# print(42/53)  ---->0.7924528302

# Relational Operators are used to comparing the values. These operators test the conditions and then returns a boolean value either True or False.

# a, b = 10, 12  
# print(a==b) # False  
# print(a<b) # True  
# print(a<=b) # True  
# print(a!=b) # True  

# Assignment operators are used to assigning values to the variables. 

# a=12  
# print(a) # 12  
# a += 2  
# print(a) # 14  
# a -= 2  
# print(a) # 12  
# a *=2  
# print(a) # 24  
# a **=2  
# print(a) # 576  

# Logical operators are used to performing logical operations like And, Or, and Not. See the example below.

# # Logical operator examples  
# a = True  
# b = False  
# print(a and b) # False  
# print(a or b) # True  
# print(not b) # True  

# Membership operators are used to checking whether an element is a member of the sequence (list, dictionary, tuples) or not. 
# Python uses two membership operators in and not in operators to check element presence.

# list = [21,24,46,17,33,54]  
# print(5 in list) # False  
# cities = ("india","delhi")  
# print("tokyo" not in cities) #True  

# Identity Operators (is and is not) both are used to check two values or variable which are located on the same part of the memory. 
# Two variables that are equal does not imply that they are identical. 
 
# a = 10   
# b = 12  
# print(a is b) # False  
# print(a is not b) # True  

# Bitwise Operators are used to performing operations over the bits. The binary operators (&, |, OR) work on bits. See the example below.

# # Identity operator example  
# a = 10   
# b = 12  
# print(a & b) # 8  
# print(a | b) # 14  
# print(a ^ b) # 6  
# print(~a) # -11  

# 3) How to create a Unicode string in Python?
# In Python 3, the old Unicode type has replaced by "str" type, and the string is treated as Unicode by default. 
# We can make a string in Unicode by using art.title.encode("utf-8") function.

# unicode_1 = ( "\U0001f638", "\u2665" ,"\u265E", "\u265F", "\u2168","\u0123")  
# print (unicode_1)  
# Output:
# unicode_1: ('ģ', '♥', '😸', '♞', '♟', 'Ⅸ')


# 4) Is Python interpreted language?
# Python is an interpreted language. The Python language program runs directly from the source code. 
# It converts the source code into an intermediate language code, which is again translated into machine language that has to be executed.
# Unlike Java or C, Python does not require compilation before execution.

# 5) How is memory managed in Python?
# Memory is managed in Python in the following ways:
# Memory management in python is managed by Python private heap space. All Python objects and data structures are located in a private heap. 
# The programmer does not have access to this private heap. The python interpreter takes care of this instead.
# The allocation of heap space for Python objects is done by Python's memory manager. The core API gives access to some tools for the programmer to code.
# Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made available to the heap space.

# 6) What is the Python decorator?
# Decorators are very powerful and a useful tool in Python that allows the programmers to add functionality to an existing code. 
# This is also called metaprogramming because a part of the program tries to modify another part of the program at compile time. 
# It allows the user to wrap another function to extend the behaviour of the wrapped function, without permanently modifying it.
# Eg.
# def call(msg):
#     return msg.upper()
# a=input("Enter your messages: \n")
# print(call(a))
# txt=call
# print(txt(a)) # Treating the function as object

# Functions vs. Decorators
# A function is a block of code that performs a specific task whereas a decorator is a function that modifies other functions.

# 7) What are the rules for a local and global variable in Python?
# Global Variables:

# Variables declared outside a function or in global space are called global variables.
# If a variable is ever assigned a new value inside the function, the variable is implicitly local, and we need to declare it as 'global' explicitly. 
# To make a variable globally, we need to declare it by using global keyword.
# Global variables are accessible anywhere in the program, and any function can access and modify its value.
# Example:

# a = "Python"  
# def function1():  
#   print(a)  
# function1()  

# Local Variables:

# Any variable declared inside a function is known as a local variable. This variable is present in the local space and not in the global space.
# If a variable is assigned a new value anywhere within the function's body, it's assumed to be a local.
# Local variables are accessible within local body only.
# Example:

# def function2():  
#     a = "Python"  
#     print(a)  
# function2()   

# 8) What is the namespace in Python?
# The namespace is a fundamental idea to structure and organize the code that is more useful in large projects. 
# A namespace is defined as a simple system to control the names in a program. It ensures that names are unique and won't lead to any conflict.
# Also, Python implements namespaces in the form of dictionaries and maintains name-to-object mapping where names act as keys and the objects as values.

# 9) What are iterators in Python?
# Iterators are used to iterate a group of elements, containers like a list. Iterators are the collection of items, and it can be a list, tuple, or a dictionary. 
# Python iterator implements __itr__ and next() method to iterate the stored elements. In Python, we generally use loops to iterate over the collections (list, tuple).
# Iterators are objects which can be traversed though or iterated upon.

# 10) What is a generator in Python?
# In Python, the generator is a way that specifies how to implement iterators. It is a normal function except that it yields expression in the function. 
# It does not implements __itr__ and next() method and reduce other overheads as well.
# If a function contains at least a yield statement, it becomes a generator. The yield keyword pauses the current execution by saving its states and then resume from the same when required.

# 11) What is slicing in Python?
# Slicing is a mechanism used to select a range of items from sequence type like list, tuple, and string. It is beneficial and easy to get elements from a range by using slice way. 
# It requires a : (colon) which separates the start and end index of the field. 
# All the data collection types List or tuple allows us to use slicing to fetch elements. Although we can get elements by specifying an index, we get only single element whereas using slicing we can get a group of elements.

# a = "Pyhton Programming!"  
# print(a[5:15])  

# 12) What is a dictionary in Python?
# The Python dictionary is a built-in data type. It defines a one-to-one relationship between keys and values. Dictionaries contain a pair of keys and their corresponding values. 
# It stores elements in key and value pairs. The keys are unique whereas values can be duplicate. The key accesses the dictionary elements.

# dict = {'Country': 'India', 'Bird': 'Peacock', 'Animal': 'Tiger'}  
# print ("Country: ", dict['Country'])    
# print ("Bird: ", dict['Bird'])  
# print ("Animal: ", dict['Animal'])  

# 13) What is Pass in Python?
# Pass specifies a Python statement without operations. It is a placeholder in a compound statement. If we want to create an empty class or functions, the pass keyword helps to pass the control without error.

# class Employee:   
#     pass # Passing class    
# class Employee:    
#     def info():  
#         pass # Passing function  

# 14) Explain docstring in Python?
# The Python docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. It provides a convenient way to associate the documentation.
# String literals occurring immediately after a simple assignment at the top are called "attribute docstrings".
# String literals occurring immediately after another docstring are called "additional docstrings".
# Python uses triple quotes to create docstrings even though the string fits on one line.
# Docstring phrase ends with a period (.) and can be multiple lines. It may consist of spaces and other special chars.

# # One-line docstrings  
# def greet():  
#     """A function to greet."""  
#     return "hello"  

# 15) What is a negative index in Python and why are they used?
# The sequences in Python are indexed and it consists of the positive as well as negative numbers. The numbers that are positive uses '0' that is uses as first index and '1' as the second index and the process go on like that.
# The index for the negative number starts from '-1' that represents the last index in the sequence and '-2' as the penultimate index and the sequence carries forward like the positive number.
# The negative index is used to remove any new-line spaces from the string and allow the string to except the last character that is given as S[:-1]. The negative index is also used to show the index to represent the string in correct order.

# 16) What is pickling and unpickling in Python?
# The Python pickle is defined as a module which accepts any Python object and converts it into a string representation. It dumps the Python object into a file using the dump function; this process is called Pickling.
# The process of retrieving the original Python objects from the stored string representation is called as Unpickling.

# 17) Which programming language is a good choice between Java and Python?
# Java and Python both are object-oriented programming languages. Let's compare both on some criteria given below:

# Criteria      	Java	        Python
# ---------------------------------------------
# Ease of use   	Good    	    Very Good
# Coding Speed	    Average	        Excellent
# Data types	    Static type	    Dynamic type
# DS & ML appl  	Average	        Very Good
# (DS-Data science, ML-Machine Learning)

# 18) What is the usage of help() and dir() function in Python?
# Help() and dir() both functions are accessible from the Python interpreter and used for viewing a consolidated dump of built-in functions.
# The help() function is used to display the documentation string and also facilitates us to see the help related to modules, keywords, and attributes.
# The dir() function is used to display the defined symbols.

# 19) What are the differences between Python 2.x and Python 3.x?
# Python 2.x is an older version of Python. Python 3.x is newer and latest version. Python 2.x is legacy now. Python 3.x is the present and future of this language.
# The most visible difference between Python2 and Python3 is in print statement (function). In Python 2, it looks like print "Hello", and in Python 3, it is print ("Hello").
# String in Python2 is ASCII implicitly, and in Python3 it is Unicode.
# The xrange() method has removed from Python 3 version. A new keyword as is introduced in Error handling.

# 20) How Python does Compile-time and Run-time code checking?
# In Python, some amount of coding is done at compile time, but most of the checking such as type, name, etc. are postponed until code execution. 
# Consequently, if the Python code references a user-defined function that does not exist, the code will compile successfully. 
# The Python code will fail only with an exception when the code execution path does not exist.