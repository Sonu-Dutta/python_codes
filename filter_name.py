"""Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]"""

#code 1
def friend(x):
    f=[]
    for i in x:
        if len(i)==4:
            f.append(i)
            
    return f
print(friend(["Sonu","Anjali","Tina"]))

#code 2
def best_friend(a):
    return [i for i in a if len(i)==4]
print(best_friend(["Mona","Priya","Renu","Yash","Rahul"]))