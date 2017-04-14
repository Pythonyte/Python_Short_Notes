'''
append is a method of a list class
which we can run in any instance of a list class

a=[1,2,3,4]
a.append(5)
it will not return anything
but will append 5 in this list a itself

so if want to add a element in empty list :
we should do like
a=[]
a.append(3)

if we do :
[].append(3)
so it will append in that list , but that list is not poinitng anywhere, so that will be lost in space

or if we do:
a=[].append(3)
again same case.
it will append in that list , but that list is not poinitng anywhere, so that will be lost in space
and none will assign to a
as append return None and append element in this list  itself
'''