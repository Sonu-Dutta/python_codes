from collections import defaultdict
name="vaishakhi"
# d={}
# for i in name:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1

d=defaultdict(int)
for i in name:
    d[i]+=1
    
print(d)