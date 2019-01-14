




class Queue:
    def __init__(self):
        self.queue = list()
        self.maxSize = 10
        self.head = 0
        self.tail = 0


    def enqueue(self, data):
        if self.size() >= self.maxSize:
            return ("Queue Full!")
        self.queue.append(data)
        self.tail += 1
        return True


    def dequeue(self):
        if self.size() <= 0:
            self.resetQueue()
            return ("Queue Empty!")
        data = self.queue[self.head]
        self.head += 1
        return data


    def size(self):
        return self.tail - self.head


    def resetQueue(self):
        self.head = 0
        self.tail = 0
        self.queue = list()





q = Queue()

print(q.enqueue(3))
print(q.enqueue(4))
print(q.enqueue(5))
print(q.enqueue(6))
print(q.enqueue(7))

print("Size before: ", q.size())

print(q.dequeue())
print(q.dequeue())

print("Size after: ", q.size())







