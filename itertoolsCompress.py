
from itertools import *
a=[1,2,3,4,5,6]
sel=[1,0,1,0,1,0]
b=compress(a,sel)
for i in b:
    print(i)