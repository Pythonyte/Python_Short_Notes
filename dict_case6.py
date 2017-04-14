'''
want to delete a key of dict , while dealing with that dict
Note: we are talking about python 3:
for better understanding :look at http://stackoverflow.com/questions/23594464/deleting-items-from-a-dictionary-with-a-for-loop
'''

#way 1 (if not dealing that dict)
d={1:11,2:22,3:33}
del d[1]
print(d)

#way 2 (if not dealing with that dict)
d={1:11,2:22,3:33}
d.pop(1)
print(d)

#way3 when dealing with dict
#example: delete keys whose values are greater than equals 3
try:
    d={'blue':1,'red':2,'yellow':3,'green':4}
    for k,v in d.items():
        if v>=3:
            del d[k]
except RuntimeError as e:
    print('Runtime Error : {}'.format(e))
'''
Above method will work for python 2  but not in python 3
bcoz while giving the keys one by one ,d,items() maintain an order of giving keys one by one.

in py2 , dict.items() provides a physical tuples not the dict object instance
but in py3:
it fetches the key and value from dict all the time, only thing it remains with it is the order of keys ( how we pass keys one by one)
SO if we delete the key in between, it will not be able to know , than what should be the next key to print.
So to keep safe, it throws run time error
'''
#this
#It will throw RuntimeError: dictionary changed size during iteration
#bcoz here in python


#pythonic way : real way

d={'blue':1,'red':2,'yellow':3,'green':4}
for key in [k for k,v in d.items() if v>=3]:
    del d[key]
print(d)

'''
gotcha
if we use generator comprehension here , instead of list comprehension
it will not work ,
bcoz it again use yeild and will give one kye one by one.
'''
