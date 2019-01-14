




class Stack:
    class MaxWithCount:
        def __init__(self, max, count):
            self.max, self.count = max, count


    def __init__(self):
        self._element = []
        self._cached_max_with_count = []


    def empty(self):
        return len(self._element) == 0


    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._cached_max_with_count[-1].max


    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        pop_element = self._element.pop()
        current_max = self._cached_max_with_count[-1].max
        if pop_element == current_max:
            self._cached_max_with_count[-1].count -= 1
            if self._cached_max_with_count[-1].count == 0:
                self._cached_max_with_count.pop()
        return pop_element


    def push(self, x):
        self._element.append(x)
        if len(self._cached_max_with_count) == 0:
            self._cached_max_with_count.append(self.MaxWithCount(x, 1))
        else:
            current_max = self._cached_max_with_count[-1].max
            if x == current_max:
                self._cached_max_with_count[-1].count += 1
            elif x > current_max:
                self._cached_max_with_count.append(self.MaxWithCount(x, 1))





s1 = Stack()

s1.push(3)
s1.push(4)
s1.push(5)
s1.push(6)

print(s1.empty())

print(s1.max())

print(s1.pop())

print(s1.max())


