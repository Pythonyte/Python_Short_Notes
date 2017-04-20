'''
__getitem__(self, key) : Defines behavior for when an item is accessed, using the notation self[key]. This is also part of both the mutable and immutable container protocols. It should also raise appropriate exceptions: TypeError if the type of the key is wrong and KeyError if there is no corresponding value for the key.


'''
class stepper:
     def __getitem__(self, i):
         return self.data[i]

X = stepper()              # X is a stepper object
X.data = "Spam"

print(X[1])                       # indexing calls __getitem__

for item in X:             # for loops call __getitem__
     print(item,end=" ")            # for indexes items 0..N


print('p' in X)                   # all call __getitem__ too


print([c for c in X])             # list comprehension

print(list(map(lambda x:x.upper(), X)))               # map calls

(a,b,c,d) = X              # sequence assignments
print(a, c, d)

print(list(X), tuple(X), ''.join(X))
#(['S', 'p', 'a', 'm'], ('S', 'p', 'a', 'm'), 'Spam')

class A:
    def __init__(self,data):
        self.data=data
    def __getitem__(self, item):
        return self.data[item]
d=A('sumit')
for x in d:
    print(x)