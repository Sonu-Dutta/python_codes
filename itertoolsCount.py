from itertools import *
# a=count(0,2)
a=count(2,4)
d=1
for i in a:
    if d>10:
        break
    else:
        print(i)
    d+=1