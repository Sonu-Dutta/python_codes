from itertools import *
a=cycle([1,2,3,4,5])
d=1
for i in a:
    if d>10:
        break
    else:
        print(i)
    d+=1
    
# b=repeat(10,3) 
# for j in b:
#     print(j)   

d=1 
b=repeat(10) 
for j in b:
    if d>10:
        break
    else:
        print(j)
    d+=1
   