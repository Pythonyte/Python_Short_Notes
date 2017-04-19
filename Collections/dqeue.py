#https://docs.python.org/3.3/library/collections.html#collections.deque
#http://book.pythontips.com/en/latest/collections.html

from collections import deque

#deck=deque()
deck=deque([1,23])
print(deck)

deck.append(33)
deck.appendleft(00)
print(deck)

deck.popleft()
deck.pop()
print(deck)

deck2=deque(maxlen=3)
deck2.extend([33,44,55])
deck2.appendleft(11)
print(deck2)