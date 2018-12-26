


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






l1 = LinkedList()


firstNode = Node("John")
l1.insertEnd(firstNode)


secondNode = Node("name in the head")
l1.insertHead(secondNode)

thirdNode = Node("name in between")
l1.insertBetween(thirdNode, 1)

l1.printList()







