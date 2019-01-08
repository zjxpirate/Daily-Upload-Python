

class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"
        self.data = data
        self.next = None
        return
    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False





class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return


    def add_list_item(self, item):
        "add to the end of the list"
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
        return


    def list_length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count


    def output_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)

            current_node = current_node.next

        return



    def search_list(self, value):

        current_node = self.head
        node_id = 1
        results = []

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)

            current_node = current_node.next
            node_id += 1

        return results




    def remove_list_item_by_id(self, item_id):
        current_id = 1
        current_node = self.head
        previous_node = None


        while current_node is not None:
            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = current_node.next
                    return
                else:
                    self.head = current_node.next
                    return

            previous_node = current_node
            current_node = current_node.next
            current_id += 1







l1 = SingleLinkedList()

l1.add_list_item(ListNode(1))
l1.add_list_item(ListNode(3))
l1.add_list_item(ListNode(5))
l1.add_list_item(ListNode(7))
l1.add_list_item(ListNode(9))



l1.remove_list_item_by_id(2)

l1.output_list()






















# class ListNode:
#     def __init__(self, data = 0, next = None):
#         self.data = data
#         self.next = next
#
#
#
# def search_list(L, key):
#     while L and L.data != key:
#         L = L.next
#
#     return L
#
#
#
# def insert_after(node, new_node):
#     new_node.next = node.next
#     node.next = new_node
#
#
#
# def delete_after(node):
#     node.next = node.next.next
#
#
# l1 = ListNode(1)
#
# print(insert_after(l1, 1))
#

