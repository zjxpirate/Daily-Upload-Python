




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


    def find(self, data):
        if self.data == data:
            return self
        if self.next == None:
            return None
        return self.next.find(data)



head = Node("Maine")
another_node = Node("Idaho")
head.next = another_node
a_third_node = Node("Utah")
another_node.next = a_third_node

print("Found: " + str(head.find("Utah").data))




