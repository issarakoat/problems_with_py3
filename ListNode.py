class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.runner = None
        self.count = 0

    def addFont(self, val):
        self.count +=1
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def append(self, val):
        self.count += 1
        newNode = ListNode(val)
        if self.head == None:
            self.head = newNode
            return

        curr = self.head
        while curr.next :
            curr = curr.next       
        curr.next = newNode

    def printList(self):
        curr = self.head
        pl = []
        while curr != None:
            pl.append(curr.val)
            curr = curr.next
        print(pl)