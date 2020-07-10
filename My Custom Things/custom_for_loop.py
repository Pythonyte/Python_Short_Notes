def MyForLoop(iterable):
    iterator = iter(iterable)
    exhaused = False
    while not exhaused:
        try:
            print(next(iterator))
        except StopIteration:
            print("_________")
            exhaused = True

def print_each(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break  # Iterator exhausted: stop the loop
        else:
            print(item)
