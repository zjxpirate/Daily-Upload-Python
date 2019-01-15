

import collections


class Queue:
    def __init__(self):
        self._data = collections.deque()

    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        return self._data.popleft()

    def max(self):
        return max(self._data)



q = Queue()

q.enqueue(5)
q.enqueue(6)
q.enqueue(7)


print("Max is: ", q.max())

print("Dequeue: ", q.dequeue())
