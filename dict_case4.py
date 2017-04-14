#counting the frequnecy of values ( dict )

colors=['black','white','blue','green','green','red','blue','white']

#normal way :
d={}
for color in colors:
    if color not in d:
        d[color]=1
    else:
        d[color]+=1
print(d)


# way 2 : if using core data types (get method) partial pythonic way
d={}

for color in colors:
    d[color]=d.get(color,0)+1

print(d)


#way3: use the inbuilt feature for these: default dict

from collections import defaultdict
d=defaultdict(int) #here int tells that values of keys will be integers.
for color in colors:
    d[color]+=1

print(d)
