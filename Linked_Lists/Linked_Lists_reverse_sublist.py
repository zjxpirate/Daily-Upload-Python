













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




def reverse_sublist(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)
    print("dummy_head: ", dummy_head)
    print("sublist_head: ", sublist_head)

    for _ in range(1, start):
        sublist_head = sublist_head.next

    print("sublist_head from start node: ", sublist_head)

    # reverses sublist.
    sublist_iter = sublist_head.next
    print("sublist_iter begin: ", sublist_iter)
    print("\n")



    count = 1
    for _ in range(finish - start):
        temp = sublist_iter.next
        print("Loop: ", count)
        print("temp: ", temp)


        print("\n")

        #1
        print("sublist_iter: ", sublist_iter)
        print("sublist_iter.next: ", sublist_iter.next)
        sublist_iter.next = temp.next
        print("temp.next: ", temp.next)
        print("sublist_iter: ", sublist_iter)

        print("\n")

        #2
        print("sublist_head: ", sublist_head)
        print("temp: ", temp)
        temp.next = sublist_head.next
        print("sublist_head.next: ", sublist_head.next)
        print("\n")

        #3
        print("sublist_head: ", sublist_head)
        sublist_head.next = temp
        print("temp: ", temp)
        print("\n")
        count += 1



    print("The result is below, above is for testing: \n")
    return dummy_head.next
















l1 = ListNode(2)

l12 = ListNode(4)
l13 = ListNode(6)
l14 = ListNode(8)
insert_after(l1, l12)
insert_after(l12, l13)
insert_after(l13, l14)



l2 = ListNode(1)

l22 = ListNode(3)
l23 = ListNode(5)
l24 = ListNode(7)
insert_after(l2, l22)
insert_after(l22, l23)
insert_after(l23, l24)



result = merge_two_sorted_lists(l1, l2)

print(reverse_sublist(result, 4, 8))












