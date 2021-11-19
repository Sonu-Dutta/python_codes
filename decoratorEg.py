def division(x,y):
    print(x/y)
def modified_div(func):
    def inner(x,y):
        if x<y:
            x,y=y,x
        return func(x,y)
    return inner
division = modified_div(division)
division(4,16)
# division(16,4)