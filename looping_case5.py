#looping over two collections:

names=['borad','chalk','duster']
colors=['black','white','blue','green']

#normal way :  old lang way
n=min(len(names),len(colors))
for i in range(n):
    print(names[i],colors[i])

#pythonic way
for name,color in zip(names,colors):
    print(name,color)
