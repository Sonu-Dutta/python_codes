from collections import OrderedDict
result=[('Sonu',98),('Anjana',99),('Sandhya',95),('Swapan',100),('Vaishakhi',90)]
d={}
for name, marks in result:
    d[name]=marks

d=OrderedDict(result)
    
print(d)
print(d.keys())
print(d.values())