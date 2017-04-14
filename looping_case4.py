#looping over indeces and values
colors=['red','green','yellow','blue']

#normal way : old lang way
for i in range(len(colors)):
    print(i,colors[i])

#pythonic way
for i,color in enumerate(colors):
    print(i,color)
