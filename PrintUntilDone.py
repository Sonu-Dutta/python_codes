value=[]
while(True):
    n=input("Enter a number: ") 
    value.append(n)
    if n=="done":
        break
value=value[:-1]
value=[int(x) for x in value]
print("Max: ",max(value))
print("Min: ",min(value))