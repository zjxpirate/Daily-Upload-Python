
class ListNode:
    def __init__(self, data=0, next=None):
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


t1 = ListNode(4)
t2 = ListNode(2)
t3 = ListNode(3)
t4 = ListNode(1)
t5 = ListNode(5)
t1.next = t2
t2.next = t3
t3.next = t4
t4.next = t5

# 13. stable sort list

def merge_two_sorted_lists(L1, L2):

    # Creates a placeholder for the result.
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    # Appends the remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummy_head.next




def stable_sort_list(L):

    # Base cases: L is empty or a single node, nothing to do.
    if not L or not L.next:
        return L

    # Find the midpoint of L using a slow and a fast pointer.
    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow

        print("in while begin")
        print("pre_slow: ", pre_slow)

        fast, slow = fast.next.next, slow.next

        print("fast: ", fast)
        print("slow: ", slow)


    print("outside")
    pre_slow.next = None  # Splits the list into two equal-sized lists.

    print("pre_slow outside")
    print("pre_slow: ", pre_slow)

    print("L: ", L)
    print ("slow: ", slow)

    print("\n")
    print("\n")

    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))


print(stable_sort_list(t1))









