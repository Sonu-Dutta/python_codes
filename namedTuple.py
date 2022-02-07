from collections import namedtuple
Color=namedtuple('Color',['red','green','blue'])
dictColor={'red':55,'green':120,'blue':245}

color1=Color(55,255,212)
white=Color(255,255,255)
black=Color(0,0,0)

print(dictColor['red'])
print(white.red)
print(black)