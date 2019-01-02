

class ListNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
        return

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False





class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
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




    def add_list_item(self, item):
        if isinstance(item, ListNode):
            if self.head is None:
                self.head = item
                item.previous = None
                item.next = None
                self.tail = item

            else:
                self.tail.next = item
                item.previous = self.tail
                self.tail = item




    def remove_list_item_by_id(self, item_id):
        current_id = 1
        current_node = self.head

        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next

            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = next_node
                    if next_node is not None:
                        next_node.previous = previous_node

                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.previous = None

                return

            current_node = next_node
            current_id += 1

        return




l1 = DoubleLinkedList()

l1.add_list_item(ListNode(1))
l1.add_list_item(ListNode(3))
l1.add_list_item(ListNode(5))
l1.add_list_item(ListNode(7))
l1.add_list_item(ListNode(9))



l1.output_list()


