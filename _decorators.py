# Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of function or class. 
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. 
 
# First Class Objects
# In Python, functions are first class objects that mean that functions in Python can be used or passed as arguments.
# Properties of first class functions:
# A function is an instance of the Object type.
# You can store the function in a variable.
# You can pass the function as a parameter to another function.
# You can return the function from a function.
# You can store them in data structures such as hash tables, lists, …

# Example 1: Treating the functions as objects.

# def greet(text): 
#     return text.upper() 
# print(greet('Namaste')) 
# say = greet 
# print(say('Namaste')) 

# Example 2: Passing the function as an argument
 
# def capital(text): 
#     return text.upper() 
# def small(text): 
#     return text.lower() 
# def greeting(func): 
#     # storing the function in a variable 
#     greet = func("""Hi, Good Morning ,everyone.""") 
#     print (greet) 
# greeting(capital) 
# greeting(small) 

# Example 3: Returning functions from another functions.
 
# def add(x): 
#     def modified_add(y): 
#         return x+y 
#     return modified_add 
# obj = add(100) 
# # print(add(100)(7)) #similar to print(obj(7)) 
# print(obj(7)) 
 
