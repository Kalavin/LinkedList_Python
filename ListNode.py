#project: LinkedList
#author: Rick Anderson

class ListNode:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return 'Node ['+str(self.data)+']'
