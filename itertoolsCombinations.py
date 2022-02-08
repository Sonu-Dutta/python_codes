from itertools import combinations, combinations_with_replacement
a=combinations('ABC',2)
b=combinations_with_replacement('ABC',2)
for i in a:
    print(i,end=" ")
print()
for j in b:
    print(j,end=" ")