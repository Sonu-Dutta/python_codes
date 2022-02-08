from itertools import zip_longest
a=[1,5,6,3,2]
b=[5,7,8]
c=zip_longest(a,b,fillvalue=10)
for i in c:
    print(i)