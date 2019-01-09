




class ListNode:

    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

    def __eq__(self, other):
        a, b = self, other
        while a and b:
            if a.data != b.data:
                return False
            a, b = a.next, b.next
        return a is None and b is None

    def __repr__(self):
        node = self
        visited = set()
        first = True

        result = ''

        while node:
            if first:
                first = False
            else:
                result += ' -> '


            if id(node) in visited:
                if node.next is not node:
                    result += str(node.data)
                    result += ' -> ... -> '

                result += str(node.data)
                result += ' -> ...'
                break
            else:
                result += str(node.data)
                visited.add(id(node))
            node = node.next

        return result


    def __str__(self):
        return self.__repr__()




def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node





def merge_two_sorted_lists(L1, L2):
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next




l1 = ListNode(4)

l12 = ListNode(6)
l13 = ListNode(8)
l14 = ListNode(10)
insert_after(l1, l12)
insert_after(l12, l13)
insert_after(l13, l14)



l2 = ListNode(5)

l22 = ListNode(7)
l23 = ListNode(9)
l24 = ListNode(11)
insert_after(l2, l22)
insert_after(l22, l23)
insert_after(l23, l24)



print(merge_two_sorted_lists(l1, l2))




