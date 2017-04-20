# generator
def uc_gen(text):
    for char in text:
        yield char.upper()

# generator expression
def uc_genexp(text):
    return (char.upper() for char in text)

# iterator protocol
class uc_iter():
    def __init__(self, text):
        self.text = text
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        try:
            result = self.text[self.index].upper()
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

# getitem method
class uc_getitem():
    def __init__(self, text):
        self.text = text
    def __getitem__(self, index):
        result = self.text[index].upper()
        return result

#To see all four methods in action:

for iterator in uc_gen, uc_genexp, uc_iter, uc_getitem:
    for ch in iterator('abcde'):
        print(ch,end=" ")
    print()

#d=uc_getitem('hello')
#print(d[1])