






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

    for _ in range(1, start):
        sublist_head = sublist_head.next

    # reverses sublist.
    sublist_iter = sublist_head.next

    for _ in range(finish - start):
        temp = sublist_iter.next

        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next






def has_cycle(head):
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step


    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next

        if slow is fast:
            # find the start of the cycle
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next


            it = head
            # both iterators advanced in tandem
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            print("Cycle found: \n")
            return it
    print("No cycle found: \n")
    return None  # No cycle












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

result.next.next.next.next.next.next.next.next = result.next.next


#print(reverse_sublist(result, 4, 8))

print(has_cycle(result))





