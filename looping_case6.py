#handling on multiple exits on loops:

a=[44,55,66,44,33,22,11,77]

#find the index of a target , if found, else return -1

#normal way : old lang way
def find(array,target):
    found=False
    for i,value in enumerate(array):
        if value == target:
            found=True
            break
    if not found:
        return -1
    else:
        return i


print(find(a,124))
print(find(a,11))


#pythonic way
#loop have else block too, which will run once your loop comes to end normally
def find(array,target):
    for i,value in enumerate(array):
        if value==target:break
    else:
        return -1
    return i

print(find(a,124))
print(find(a,11))
