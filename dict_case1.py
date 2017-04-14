#print keys of dict

d={'a':11,'b':22,'c':33}

for k in d:
    print(k)

print({k:d[k] for k in d if not k.startswith('b')})
