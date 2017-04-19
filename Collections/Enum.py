#https://docs.python.org/3.4/library/enum.html
#An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.
from enum import Enum
class Shake(Enum):
    mango=25
    milk=20
    banana=30
    sapota=40

#now Shake is an enumeration: this is not the class Type: its Enum type
print('{} => {}'.format(Shake,list(Shake)))

#each class attribute are enum members..
for shake in Shake:
    print(shake,type(shake),isinstance(shake,Shake))

#now every object ahev two attributes name and value
print(Shake.mango.name,Shake.mango.value)

#two enum members are allowed to have the same value. Given two members A and B with the same value (and A defined first), B is an alias to A. By-value lookup of the value of A and B will return A. By-name lookup of B will also return A:
class Shape(Enum):
    square = 2
    diamond = 1
    circle = 3
    alias_for_square = 2

print(Shape.square.name,Shape.square.value)
print(Shape.alias_for_square.name,Shape.alias_for_square.value)
