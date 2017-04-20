class Myrange:
    def __init__(self,low,high):
        self.low=low
        self.high=high

    def __iter__(self):
        return self

    def __next__(self):
        if self.low>self.high:
            raise StopIteration
        else:
            self.low+=1
            return self.low-1

Obj=Myrange(6,8)
print(Obj)

for i in Obj:
    print(i)

'''
We created the object of our class i.e.
when we passed it to for loop..
first for loop tries to call iter mathod to that object to get the iterator.
As we have __iter__ mathod available in our class.. we will get iterator
then form loop call the next till it will not get the Stopiteration exception.
ASo it will go to the next function and return the expected values..

Iterator objects in python conform to the iterator protocol, which basically means they provide two methods: __iter__() and  next(). The __iter__ returns the iterator object and is implicitly called at the start of loops. The next() method returns the next value and is implicitly called at each loop increment.  next() raises a StopIteration exception when there are no more value to return, which is implicitly captured by looping constructs to stop iterating.
'''

