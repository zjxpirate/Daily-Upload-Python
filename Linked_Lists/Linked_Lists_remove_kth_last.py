






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



def overlapping_no_cycle_lists(l0, l1):
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length

    l0_len, l1_len = length(l0), length(l1)

    if l0_len > l1_len:
        l0, l1 = l1, l0 # l1 is the longer list

    # Advance the longer list to get equal length lists.
    for _ in range(abs(l0_len - l1_len)):
        l1 = l1.next

    while l0 and l1 and (l0.data is not l1.data):
        l0, l1 = l0.next, l1.next

    print("\n")
    print("None means no overlapping, otherwise the part that overlaps print below: ")
    return l0 #None implies there is no overlapping between l0 and l1.







def overlapping_lists(l0, l1):

    # Store the start of cycle if any.
    root0, root1 = has_cycle(l0), has_cycle(l1)

    if not root0 and not root1:
        # both lists don't have cycles.
        return overlapping_no_cycle_lists(l0, l1)

    elif (root0 and not root1) or (not root0 and root1):
        # One list has cycle, one list has no cycle.
        return None

    # Both lists have cycles.
    temp = root1
    while True:
        temp = temp.next
        if temp is root0 or temp is root1:
            break


    # l0 and l1 do not end in the same cycle.
    # if temp is not root0:
    #     print(temp is not root0)
    #     return None  # Cycle are disjoint.


    # Calculate the distance betweeen a and b.
    def distance(a, b):
        dis = 0
        while a is not b:
            a = a.next
            dis += 1
        return dis



    # l0 and l1 end in the same cycle, locate the overlapping node if they
    # first overlap before cycle starts.
    stem0_length, stem1_length = distance(l0, root0), distance(l1, root1)
    if stem0_length > stem1_length:
        l1, l0 = l0, l1
        root0, root1 = root1, root0
    for _ in range(abs(stem0_length - stem1_length)):
        l1 = l1.next
    while l0 is not l1 and l0 is not root0 and l1 is not root1:
        l0, l1 = l0.next, l1.next



    # If l0 == l1 before reaching root0, it means the overlap first occurs
    # before the cycle starts; otherwise, the first overlapping node is not
    # unique, we can return any node on the cycle.
    return l0 if l0 is l1 else root0


def deletion_from_list(node_to_delete):
    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next




def remove_kth_last(L, k):
    dummy_head = ListNode(0, L)
    first = dummy_head.next
    for _ in range(k):
        first = first.next
    print("first node: ", first)
    second = dummy_head
    print("second node: ", second)
    while first:
        first, second = first.next, second.next

    # Second points to the (k + 1)-th last node, deletes its successor.
    second.next = second.next.next
    return dummy_head.next









l1 = ListNode(2)

l12 = ListNode(4)
l13 = ListNode(6)
l14 = ListNode(8)
l15 = ListNode(10)
insert_after(l1, l12)
insert_after(l12, l13)
insert_after(l13, l14)
insert_after(l14, l15)



l2 = ListNode(1)

l22 = ListNode(3)
l23 = ListNode(5)
l24 = ListNode(7)
l25 = ListNode(9)
insert_after(l2, l22)
insert_after(l22, l23)
insert_after(l23, l24)
insert_after(l24, l25)


result = merge_two_sorted_lists(l1, l2)

#result.next.next.next.next.next.next.next.next = result.next.next


#print(reverse_sublist(result, 4, 8))

#print(has_cycle(result))


#print(overlapping_no_cycle_lists(l1, l2))


# l1.next.next.next.next.next = l1.next.next
# l2.next.next.next.next.next = l2.next.next
#
#
# print(overlapping_lists(l1, l2))

# print(l1)
#
# deletion_from_list(l12)
#
# print(l1)


print(result)

remove_kth_last(result, 3)

print(result)











