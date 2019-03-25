




class Queue:

    def __init__(self):
        self._enq, self._deq = [], []


    def enqueue(self, x):
        self._enq.append(x)


    def dequeue(self):
        if not self._deq:
            # Transfer the elements in _enq to _deq.
            while self._enq:
                self._deq.append(self._enq.pop())

        if not self._deq:  # _deq is still empty!
            raise IndexError('empty queue')

        return self._deq.pop()



    def printQueue(self):
        return self._deq




q = Queue()

q.enqueue(4)
q.enqueue(5)
q.enqueue(6)




print(q.dequeue())

print(q.printQueue())
