#looping over keys and values of dict

#normal way :
d={'a':11,'b':22,'c':33}
for k in d:
    print(k,d[k])

#pythonic way
for k,v in d.items():
    print(k,v)