




class Queue:

    SCALE_FACTOR = 2

    def __init__(self, capacity):
        self._entries = [None] * capacity
        self._head = self._tail = self._num_queue_elements = 0


    def enqueue(self, x):
        if self._num_queue_elements == len(self._entries):   # Needs to resize.
            # Makes the queue elements appear consecutively.
            self._entries = (self._entries[self._head:] + self._entries[:self._head])

            # Resets head and tail.
            self._head, self._tail = 0, self._num_queue_elements
            self._entries += [None] * (len(self._entries) * Queue.SCALE_FACTOR - len(self._entries))

        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_queue_elements += 1




    def dequeue(self):
        if not self._num_queue_elements:
            raise IndexError('empty queue')
        self._num_queue_elements -= 1
        result = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return result




    def size(self):
        return self._num_queue_elements


    def printQueue(self):
        return self._entries



q = Queue(10)



q.enqueue(5)
q.enqueue(7)
q.enqueue(15)
q.enqueue(22)
q.enqueue(9)

print(q.printQueue())

print("Here is the size: ", q.size())


print("dequeue: ", q.dequeue())

print("Here is new queue: ", q.size())