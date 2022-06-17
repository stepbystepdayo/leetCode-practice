class listNode:
    def __init__(self,value=0, next=None):
        self.value = value
        self.next = None
class solution:
    def reverseList(self,head):
        # current is head and prev is None 
        cur = head
        prev = None

        # when cur is None, this loop will finish
        while cur is not None:
            # this old_cur is head's pointer's next
            old_cur = cur.next

            # this cur.next thats mean head's next will be prev that None(before head)
            cur.next = prev

            # priviouse prev became head and the flow of arrows will be reversed. so prev will be cur(its priviouse head)
            prev = cur

            # then, cur will be old_cur(thats cur.next)
            cur = old_cur

        return prev



