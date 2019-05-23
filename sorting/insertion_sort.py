
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

# 12. insertion sort

def insertion_sort(L):
    dummy_head = ListNode(0, L)


    # the sublist consisting of nodes up to and including iter is sorted in
    # increasing order. we need to ensure that after we move to L.next with its
    # property continue to hold. we do this by swapping L.next with its
    # predecessors in the list till it's in the right place.
    print("L: ", L)
    print("dummy_head: ", dummy_head)

    while L and L.next:
        if L.data > L.next.data:
            target, pre = L.next, dummy_head

            print("target: ", target)
            print("pre: ", pre)


            # print("test sart from here:")
            # pre.next = target
            # print(pre)
            # print(dummy_head)


            print("1: ", pre.next.data)
            print("2: ", target.data)

            while pre.next.data < target.data:
                pre = pre.next

                print("pre = pre.next: ", pre)

            temp = pre.next

            print("temp: ", temp)
            print("pre: ", pre)
            print("L: ", L)
            print("target: ", target)
            print("dummy", dummy_head)
            print("\n")

            print("dummy", dummy_head)
            pre.next = target
            print("dummy", dummy_head)
            print("pre.next: ", pre.next)
            print("temp: ", temp)
            print("pre: ", pre)
            print("L: ", L)
            print("target: ", target)

            print("\n")


            print("temp: ", temp)
            L.next = target.next


            print("L.next: ", L.next)
            print("temp: ", temp)
            print("pre: ", pre)
            print("L: ", L)
            print("target: ", target)
            print("dummy", dummy_head)
            print("\n")


            target.next = temp

            print("target.next: ", target.next)
            print("temp: ", temp)
            print("pre: ", pre)
            print("L: ", L)
            print("target: ", target)
            print("dummy", dummy_head)

        else:
            L = L.next
            print("L = L.next: ", L)

        print("\n")
        print("\n")

    return dummy_head.next

print(insertion_sort(t1))



