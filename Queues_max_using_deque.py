

import collections



class QueueWithMax:

    def __init__(self):
        self._entries = collections.deque()
        self._candidates_for_max = collections.deque()


    def enqueue(self, x):
        self._entries.append(x)
        # Eliminate dominated elements in _candidates_for_max.
        while self._candidates_for_max and self._candidates_for_max[-1] < x:
            self._candidates_for_max.pop()
        self._candidates_for_max.append(x)



    def dequeue(self):
        if self._entries:
            result = self._entries.popleft()
            if result == self._candidates_for_max[0]:
                self._candidates_for_max.popleft()
            return result
        raise IndexError('empty queue')



    def max(self):
        if self._candidates_for_max:
            return self._candidates_for_max[0]
        raise IndexError('empty queue')



    def head(self):
        return self._entries[0]





q = QueueWithMax()



q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(56)
q.enqueue(12)
q.enqueue(2)


print("Head: ", q.head())
print("Max: ", q.max())








