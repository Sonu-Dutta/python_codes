# Pickle comes in handy while saving complicated data. They are easy to use, lighter, and do not require several lines of code. 
# The pickled file generated is not easily readable and thus provides some level of security. 

# What is pickling?
# Pickling is the process of serializing an object. Serializing means storing the object in the form of binary representation so it can be saved in our main memory. 
# The object could be of any type. It could be a string, tuple, or any other sort of object that Python supports. 
# The data is stored in the main memory in a file. While writing the code for pickling, we open the file in "wb" mode, also known as writing binary mode. 
# So, to use the pickle module, we have to make a file with the .pkl extension and send it in a dump() function along with the object. dump() is a built-in function in the Pickle module, made for pickling.

import pickle

# dict1 = { 'Name': 'Anjana', 'Salary':90000, 'Profession': 'Interior-Designer' } 
# myfile = open('emp.pkl','wb') 
# pickle.dump(dict1,myfile) 
# myfile.close()


# What is unpickling?
# The file format is binary, so we cannot directly open and read it; instead, we have to open it using a python program, and the process is known as unpickling. 
# We have to open the file in "rb" mode for unpickling, also known as a read binary mode. The function we use this time is also a built-in function, named load(). 
# Unlike dump(), we have to send the file name as a parameter, and it automatically retrieves the data in the object type it was inserted in. 
# For example, if we send a list while pickling, the return result will also be a list.

# myfile = open('emp.pkl','rb') 
# dict1 = pickle.load(myfile) 
# print(dict1)
# myfile.close()


# Disadvantages:

# There are some situations in which pickling is discouraged. For example, when we are working with multiple programming languages, pickle is discouraged.
# Pickle has been found slower than its alternatives.
# In some cases, it has also shown a few security vulnerabilities.
# When we update our program to a newer version, pickled data through the previous version can cause issues.

