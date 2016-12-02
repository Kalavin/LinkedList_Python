from ListNode import ListNode


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert(self, x):
        self.insertAtRear(x)

    def insertAtRear(self, x):
        if (self.head == None):
            self.head = ListNode(x, None, None)
            self.tail = self.head
        else:
            tmp = ListNode(x, None, None)
            self.tail.next = tmp
            tmp.prev = self.tail
            self.tail = tmp
        self.count += 1

    def insertAtFront(self, x):
        if(self.head == None):
            self.insertAtRear(x)
        else:
            tmp = ListNode(x, None, None)
            self.head.prev = tmp
            tmp.next = self.head
            self.head = tmp
            self.count += 1

    def size(self):
        return self.count

    def find(self, x):
        current = self.head
        while(current != None):
            if(current.data == x):
                return current
            current = current.next
        return None

    def remove(self, x):
        current = self.find(x)
        if(current == None):
            print('Node does not exist')
            return
        if(current.prev != None):
            current.prev.next = current.next
        else:
            self.head = current.next
        if(current.next != None):
            current.next.prev = current.prev
        else:
            self.tail = current.prev
        self.count -= 1

    def removeFront(self):
        self.head.next.prev = None
        self.head = self.head.next
        self.count -= 1

    def removeRear(self):
        self.tail.prev.next = None
        self.tail = self.tail.prev
        self.count -= 1

    def enqueue(self, x):
        self.insertAtRear(x)

    def dequeue(self):
        tmp = self.head
        self.removeFront()
        return tmp.data

    def push(self, x):
        self.insertAtRear(x)

    def pop(self):
        tmp = self.tail
        self.removeRear()
        return tmp

    def get(self, index):
        if index > self.count or index < 0:
            print('index is out of bounds')
            return None
        current = self.head
        for i in range(0,index):
            current = current.next
        return current.data

    def indexOf(self,x):
        current = self.head
        count = 0
        while (current != None):
            if (current.data == x):
                return count
            current = current.next
            count += 1
        return -1

    def printList(self):
        current = self.head
        while(current != None):
            print(current.data)
            current = current.next