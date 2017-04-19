from collections import Counter

a='helloo'
c=Counter(a)
print(c,list(c.elements()))

a=[11,22,33,22,11,343,5]
c=Counter(a)
print(c,list(c.elements()))

a={'red':3,'blue':1}
c=Counter(a)
print(c,list(c.elements()))

#when we try to get value of non existing key: it will return 0
print(c['yellow'])

