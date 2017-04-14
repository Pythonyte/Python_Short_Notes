colors=['red','green','yellow','blue']

#look backword in list
#normal way : old lang way
for i in range(len(colors)-1,-1,-1):
    print(colors[i])


#pythonic way :
#again reversed will return an iterator:
for color in reversed(colors):
    print(color)


