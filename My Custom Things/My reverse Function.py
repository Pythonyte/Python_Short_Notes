class MyReverse:
    def __init__(self,seq):
        self.seq=seq
        self.idx=-1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result=self.seq[self.idx]
        except IndexError:
            raise StopIteration
        else:
            self.idx-=1
            return result

arr=[11,22,33,44,12]
for i in MyReverse(arr):
    print(i)




