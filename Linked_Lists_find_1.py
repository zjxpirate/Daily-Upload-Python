




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


    def find(self, data):
        current = self
        while(current != None):
            if current.data == data:
                return current
            current = current.next

        return None



head = Node("Maine")
another_node = Node("Idaho")
head.next = another_node
a_third_node = Node("Utah")
another_node.next = a_third_node


print("Found: " + str(head.find("Utah").data))




