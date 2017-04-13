class SingleInstance:
    _instance=None
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            #cls._instance = super(SingleInstance, cls).__new__(cls)
            cls._instance = super().__new__(cls)
        return cls._instance

s=SingleInstance()
print(hasattr(SingleInstance, '_instance'))
print(SingleInstance.__dict__)
print(type(s))

s2=SingleInstance()
print(hasattr(SingleInstance, '_instance'))
print(SingleInstance.__dict__)
print(type(s2))

print(s is s2)


'''
A slightly different approach to implement the singleton in Python is the borg pattern by Alex Martelli (Google employee and Python genius).
'''
class Way2:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state
'''
So instead of forcing all instances to have the same identity, they share state.
'''

b1=Way2()
b2=Way2()
b1.a=122
print(b1.__dict__,b2.__dict__)

