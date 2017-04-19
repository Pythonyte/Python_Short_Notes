'''
Usually, a Python dictionary throws a KeyError if you try to get an item with a key that is not currently in the dictionary. The defaultdict in contrast will simply create any items that you try to access (provided of course they do not exist yet). To create such a "default" item, it calls the function object that you pass in the constructor (more precisely, it's an arbitrary "callable" object, which includes function and type objects). For the first example, default items are created using int(), which will return the integer object 0. For the second example, default items are created using list(), which returns a new empty list object.
'''
from collections import defaultdict

#example1
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d1=defaultdict(list)
for k,v in s:
    d1[k].append(v)
print(d1)

#example2
s='trip on tiago'
d2=defaultdict(int)
for char in s:
    d2[char]+=1
print(d2)

#example3: any callable object
fun=lambda : 'Test value'
d3=defaultdict(fun)
print(d3['key1'])
print(d3)

#great example for nested dict:
#{  a : {b: {c : 1} }, x : {y : { z: 1 } }  }
nestedFun=lambda : defaultdict(nestedFun)
d4=nestedFun()
d4['a']['b']['c']=1
d4['x']['y']['z']=1
print(d4)
