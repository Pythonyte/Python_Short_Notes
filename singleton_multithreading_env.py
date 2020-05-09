import threading

lock = threading.Lock()


class SingletonClass(object):
    _instances = {}
    def __new__(cls, *args, **kwargs):
        """
        This check, (first check) is for avoid unnecessary locking, once instance is
        set in _instances in dict
        """
        if cls not in cls._instances:
            # CheckPoint 1
            with lock:
                """
                This check, (second check) if needed for overriding _instances dict update:
                Scenario:
                    multiple threads came to CheckPoint 1 at almost near same time.
                    Now one thread got the lock, came inside critical section and
                    updates _instances dict with newly created instance and then 
                    releases the lock.

                    Now second thread got the lock, Now think....
                    if this second check is not there, this second thread will create new instance
                    and update the dict (which we really dont want)
                """
                if cls not in cls._instances:
                    cls._instances[cls] = super(SingletonClass, cls).__new__(cls, *args, **kwargs)

        return cls._instances[cls]

#
# def testThread(num):
#     print("Object value", SingletonClass())
#
#
# if __name__ == '__main__':
#     for i in range(5):
#         t = threading.Thread(target=testThread, args=[i])
#         t.start()

print(SingletonClass())
print(SingletonClass())
print(SingletonClass())
