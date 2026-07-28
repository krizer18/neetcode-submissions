class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
           
            i += 1
            curr = curr.next
        return -1


        


    def insertHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head.next
        self.head.next = new
        if new.next == None:
            self.tail = new
        

    def insertTail(self, val: int) -> None:
        new = ListNode(val)
        self.tail.next = new
        self.tail = new
        

    def remove(self, index: int) -> bool:
        i = 0 
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

        

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head.next
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr
        
