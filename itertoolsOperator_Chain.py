from itertools import accumulate, chain
import operator
a=[1,2,3,4,5,6]
# b=accumulate(a)
b=accumulate(a,operator.mul)
for i in b:
    print(i)
    
c=[10,20,30,40]    
a=chain(a,c)
for i in a:
    print(i)