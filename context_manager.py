import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

class changeDir(object):
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.cwd = os.getcwd()
        os.chdir(self.path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.cwd)


with changeDir('/home/sumit/Documents/misc-codes/lc'):
    print(os.listdir())

with changeDir('/home/sumit/Documents/misc-codes/msqs'):
    print(os.listdir())

print(os.getcwd())