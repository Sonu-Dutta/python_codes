# The range() and xrange() are two functions that could be used to iterate a certain number of times in for loops in Python. 
# In Python 3, there is no xrange , but the range function behaves like xrange in Python 2.
# If you want to write code that will run on both Python 2 and Python 3, you should use range().

# range() – This returns a range object (a type of iterable).
# xrange() – This function returns the generator object that can be used to display numbers only by looping. 
# The only particular range is displayed on demand and hence called “lazy evaluation“.
# Because of the fact that xrange() evaluates only the generator object containing only the values that are required by lazy evaluation, therefore is faster in implementation than range().

# a = range(1,100)
# b = xrange(1,100)
 
# print ("The return type of range() is : ")
# print (type(a))
 
# print ("The return type of xrange() is : ")
# print (type(b))

# Output:

# The return type of range() is : 
# <type 'list'>
# The return type of xrange() is : 
# <type 'xrange'>

# The variable storing the range created by range() takes more memory as compared to the variable storing the range using xrange(). 
# The basic reason for this is the return type of range() is list and xrange() is xrange() object.

# As range() returns the list, all the operations that can be applied on the list can be used on it. 
# On the other hand, as xrange() returns the xrange object, operations associated to list cannot be applied on them, hence a disadvantage.