




import functools

from list_node import ListNode


def insert_after(node, new_node):
    new_node = ListNode(new_node)
    new_node.next = node.next
    node.next = new_node



a = ListNode(4)
a = ListNode(5)

insert_after(a, 6)

print(a)
