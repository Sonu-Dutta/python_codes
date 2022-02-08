from itertools import product

a=product('ABCD',repeat=2)
for i in a:
    print(i)