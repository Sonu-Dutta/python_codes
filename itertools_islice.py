
from itertools import islice
a=list(range(0,100,5))
print(a,end=" ")
print()
b=islice(a,0,15,3)
for i in b:
    print(i, end=" ")
