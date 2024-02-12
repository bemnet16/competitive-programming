class Node:
    def __init__(self,val):
        self.val = val
        self.next = None



class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        
        if not self.head:
            return -1
        
        if index == 0 and self.head:
            return self.head.val
        
        count = 0
        cur = self.head
        while cur.next:
            cur = cur.next
            count += 1
            if count == index:
                return cur.val
        
        return -1
            
    def addAtHead(self, val: int) -> None:
        
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return 
        
        new_node.next = self.head
        self.head = new_node
        
        return

    def addAtTail(self, val: int) -> None:
        
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        
        cur = self.head
        while cur and cur.next:
            cur = cur.next
        
        cur.next = new_node
        
        return

    def addAtIndex(self, index: int, val: int) -> None:
        
        new_node = Node(val)
        if not self.head and index == 0:
            self.head = new_node
            return
        
        if index == 0 and self.head:
            new_node.next = self.head
            self.head = new_node
            return
            
        cur = self.head
        count = 0
        while cur:
            count += 1
            if count == index:
                new_node.next = cur.next
                cur.next = new_node
            cur = cur.next

        return

    def deleteAtIndex(self, index: int) -> None:
        
        if not self.head:
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        cur = self.head
        count = 0
        while cur:
            count += 1
            if count == index:
                if cur.next:
                    cur.next = cur.next.next
            cur = cur.next
            
        return
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)