




class circularQueue:
    def __init__(self):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = 10


    def enqueue(self, data):
        if self.size() == self.maxSize - 1:
            return ("Queue Full!")
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.maxSize
        return True


    def dequeue(self):
        if self.size() == 0:
            return ("Queue Empty!")
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        return data


    def size(self):
        if self.tail >= self.head:
            return (self.tail - self.head)
        return (self.maxSize - (self.head - self.tail))





q = circularQueue()

print(q.enqueue(4))
print(q.enqueue(5))
print(q.enqueue(6))
print(q.enqueue(7))
print(q.enqueue(8))

print("Size before: ", q.size())

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print("Size after: ", q.size())






