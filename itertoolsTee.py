from itertools import tee
a=[1,2,3,4,5]
at=iter(a)
b=tee(at,3)
for i in b:
    print(list(i))
