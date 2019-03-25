






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




def remove_duplicates(L):

    it = L
    while it:
        # Uses next_distinct to find the next distinct value.
        next_distinct = it.next
        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = next_distinct
    return L




def cyclically_right_shift_list(L, k):
    if not L:
        return L

    # Computes the length of the L and the tail
    tail, n = L, 1
    while tail.next:
        n += 1
        tail = tail.next

    k %= n
    if k == 0:
        return L


    tail.next = L   # Makes a cycle by connecting the tail to the head.
    steps_to_new_head, new_tail = n - k, tail

    while steps_to_new_head:
        steps_to_new_head -= 1
        new_tail = new_tail.next


    new_head = new_tail.next
    new_tail.next = None
    return new_head




def even_odd_merge(L):

    if not L:
        return L


    even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0
    print("tails is here: ", tails[1])
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1   # Alternate between even and odd.
        print(turn)

    tails[1].next = None
    tails[0].next = odd_dummy_head.next

    print("\n")
    print("Here is the result: ")
    return even_dummy_head.next



def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev




def is_linked_list_a_palindrome(L):

    # Finds the second half of L.
    slow = fast = L
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    # Compares the first half and the reversed second half lists.
    first_half_iter, second_half_iter = L,reverse_linked_list(slow)
    while second_half_iter and first_half_iter:
        if second_half_iter.data != first_half_iter.data:
            return False
        second_half_iter, first_half_iter = (second_half_iter.next, first_half_iter.next)

    return True




def list_pivoting(l, x):

    less_head = less_iter = ListNode()
    equal_head = equal_iter = ListNode()
    greater_head = greater_iter = ListNode()

    # Populates the three lists.
    while l:
        if l.data < x:
            less_iter.next = l
            less_iter = less_iter.next
        elif l.data == x:
            equal_iter.next = l
            equal_iter = equal_iter.next
        else:   # l.data > x.
            greater_iter.next = l
            greater_iter = greater_iter.next
        l = l.next


    # Combines the three lists
    greater_iter.next = None
    equal_iter.next = greater_head.next
    less_iter.next = equal_head.next
    return less_head.next




def add_two_numbers(l1, l2):

    place_iter = dummy_head = ListNode()
    carry = 0

    while l1 or l2 or carry:
        val = carry + (l1.data if l1 else 0) + (l2.data if l2 else 0)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        place_iter.next = ListNode(val % 10)
        carry, place_iter = val // 10, place_iter.next

    return dummy_head.next













l1 = ListNode(5)

l12 = ListNode(1)
l13 = ListNode(0)
l14 = ListNode(3)
l15 = ListNode(8)
insert_after(l1, l12)
insert_after(l12, l13)
insert_after(l13, l14)
insert_after(l14, l15)



l2 = ListNode(8)

l22 = ListNode(4)
l23 = ListNode(6)
l24 = ListNode(7)
l25 = ListNode(1)
insert_after(l2, l22)
insert_after(l22, l23)
insert_after(l23, l24)
insert_after(l24, l25)




l3 = ListNode(0)

l32 = ListNode(2)
l33 = ListNode(4)
l34 = ListNode(2)
l35 = ListNode(0)
insert_after(l3, l32)
insert_after(l32, l33)
insert_after(l33, l34)
insert_after(l34, l35)




#result = merge_two_sorted_lists(l1, l2)

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

# print(result)
#
# remove_kth_last(result, 3)
#
# print(result)

# print(result)
#
# remove_duplicates(result)
#
# print(result)

# print(result)
#
# print(cyclically_right_shift_list(result, 2))

# print(result)
#
# print(even_odd_merge(result))


# print(l3)
# print(is_linked_list_a_palindrome(l3))
#
# print("\n")
#
# print(result)
# print((is_linked_list_a_palindrome(result)))



# print(l2)
#
# print(list_pivoting(l2, 6))


print(l1)
print("\n")
print(l2)
print("\n")
print("Here is the result: ", add_two_numbers(l1, l2))














