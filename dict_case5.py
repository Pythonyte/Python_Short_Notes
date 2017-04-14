'''
grouping with dict
Example:
    name=['sumit','soni','vikram','jim','jagap','mayur','pradep']
    I want to group names according to their length.
'''

names=['sumit','soni','vikram','jim','jagap','mayur','pradep']

#normal way:
d={}
for name in names:
   key=len(name)
   if key not in d:
       d[key]=[]
   d[key].append(name)
print(d)

#next way :
d={}
for name in names:
   key=len(name)
   d.setdefault(key,[])
   d[key].append(name)
print(d)


#next way :
d={}
for name in names:
   key=len(name)
   d.setdefault(key,[])
   d[key].append(name)
print(d)


#last way: pythonic way
from collections import defaultdict
d=defaultdict(list) # here list will tell that: values of keys will be list
for name in names:
    key=len(name)
    d[key].append(name)
print(d)
