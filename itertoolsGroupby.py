from itertools import groupby

a=[(2,3),(7,8),(4,6),(3,7)]
func_key=lambda x:x[1]
b=groupby(a,func_key)
for i,j in b:
    print(i,list(j))