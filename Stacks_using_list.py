




class Stack:
    def __init__(self):
        self.stack = list()


    def push(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        return False


    def pop(self):
        if len(self.stack) <= 0:
            return("Stack Empty!")
        return self.stack.pop()


    def size(self):
        return len(self.stack)


myStack = Stack()


print(myStack.push(4))
print(myStack.push(5))
print(myStack.push(6))

print(myStack.size())

print(myStack.pop())

print(myStack.size())


