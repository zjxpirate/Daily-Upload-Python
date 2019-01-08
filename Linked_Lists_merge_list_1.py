


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next

        return length

    def isListEmpty(self):
        if self.listLength() == 0:
            return True
        else:
            return False

    def insertHead(self, newNode):
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode

    def insertBetween(self, newNode, position):
        if position < 0 or position > self.listLength():
            print("Invalid position")
            return
        if position is 0:
            self.insertHead(newNode)
            return

        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            print("List is empty delete failed")

    def deleteBetween(self, position):
        if position < 0 or position >= self.listLength():
            print("Invalid position")
            return
        if self.isListEmpty() is False:
            if position is 0:
                self.deleteHead()
                return
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1

    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

    def printList(self):

        if self.head is None:
            print("List is empty")
            return

        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    def mergeLists(self, firstList, secondList, mergedList):

        currentFirst = firstList.head
        currentSecond = secondList.head



        while True:
            if currentFirst is None:
                mergedList.insertEnd(currentSecond)
                break

            if currentSecond is None:
                mergedList.insertEnd(currentFirst)
                break

            if currentFirst.data < currentSecond.data:
                currentFirstNext = currentFirst.next
                currentFirst.next = None
                mergedList.insertEnd(currentFirst)
                currentFirst = currentFirstNext

            else:
                currentSecondNext = currentSecond.next
                currentSecond.next = None
                mergedList.insertEnd(currentSecond)
                currentSecond = currentSecondNext


list1 = LinkedList()
list2 = LinkedList()

list1.insertEnd(Node(1))
list1.insertEnd(Node(3))
list1.insertEnd(Node(5))
list1.insertEnd(Node(7))
list1.insertEnd(Node(16))
list1.insertEnd(Node(18))
list1.insertEnd(Node(32))

list2.insertEnd(Node(2))
list2.insertEnd(Node(8))
list2.insertEnd(Node(16))
list2.insertEnd(Node(23))
list2.insertEnd(Node(30))
list2.insertEnd(Node(31))

l3 = LinkedList()

l3.mergeLists(list1, list2, l3)

l3.printList()







