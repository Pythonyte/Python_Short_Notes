for i in [0,1,2,3,4,5]:
    print(i)

for i in range(6):
    print(i)

'''
Even for 1 million hold , range operator will do .next operation and provide 1 value at a time.
It will not hold 1 million records at a time.
'''

'''
>>> a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> a.__sizeof__()
440
>>> range(50).__sizeof__()
48

>>> reversed(a)
<list_reverseiterator object at 0x000001E2F436F0F0>
>>> reversed(a).__sizeof__()
32
>>> list(reversed(a)).__sizeof__()
536
>>> list(reversed(a))
[49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


which shows that, iterators are using very less memory as they take one value at a time .not the whole physical list.

'''