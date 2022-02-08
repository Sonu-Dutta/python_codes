from itertools import dropwhile, takewhile, filterfalse

a=list(range(0,50,5))
b=dropwhile(lambda x:x<20,a)
c=takewhile(lambda y:y<20,a)
d=filterfalse(lambda z:z<20,a)
for i in b:
    print(i,end=" ")
print()    
for j in c:
    print(j,end=" ")
print()
for k in d:
    print(k,end=" ")