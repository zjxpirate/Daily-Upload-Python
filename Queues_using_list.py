




class Queue:
    def __init__(self):
        self.queue = list()


    def enqueue(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False


    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("Queue Empty!")


    def size(self):
        return len(self.queue)


    def printQueue(self):
        return self.queue








q = Queue()

print(q.enqueue(5))
print(q.enqueue(6))
print(q.enqueue(7))
print(q.enqueue(8))
print(q.enqueue(9))
print(q.printQueue())

print(q.size())


print(q.dequeue())
print(q.dequeue())

print(q.size())

print(q.printQueue())



