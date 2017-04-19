'''
what are namedtuples? They turn tuples into convenient containers for simple tasks. With namedtuples you don’t have to use integer indexes for accessing members of a tuple. You can think of namedtuples like dictionaries but unlike dictionaries they are immutable.
https://docs.python.org/3.3/library/collections.html#collections.namedtuple

Collections.namedtuple(typename, field_names, verbose=False, rename=False)
Returns a new tuple subclass named typename. The new subclass is used to create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable. Instances of the subclass also have a helpful docstring (with typename and field_names) and a helpful __repr__() method which lists the tuple contents in a name=value format.
'''


from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
jerry = Animal("jerry", 11, "mouse")

print(perry)
# Output: Animal(name='perry', age=31, type='cat')

print(perry[0])
print(perry.name)



#you cant change the values once it is set. (its immutable)
try:
    jerry.name=44
except AttributeError as e:
    print(e)

print(jerry,jerry.name)

