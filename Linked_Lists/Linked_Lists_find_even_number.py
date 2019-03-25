




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None




head = Node(0)
current = head
for i in range(1, 51):
    current.next = Node(2 * i)
    current = current.next


current = head
while current != None:
    print(current.data)
    current= current.next




