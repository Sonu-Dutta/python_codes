from itertools import starmap

a=[(10,12),(13,24),(55,60),(75,28)]
b=starmap(lambda x,y:(x+5,y+2),a)
for i in b:
    print(i)