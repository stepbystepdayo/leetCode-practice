'''

  You're given the head of a Singly Linked List whose nodes are in sorted order
  with respect to their values. Write a function that returns a modified version
  of the Linked List that doesn't contain any nodes with duplicate values. The
  Linked List should be modified in place (i.e., you shouldn't create a brand
  new list), and the modified Linked List should still have its nodes sorted
  with respect to their values.

  Each LinlkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of thr list.

'''
class LinkList:
    def __init__(self,value):
        self.value = value
        self.next = None

def solution(linkedList):
    
    currentNode = linkedList
    while currentNode is not None:
        nextDist = currentNode.next
        while nextDist is not None and nextDist.value == currentNode.Value:
            nextDist = nextDist.next

        currentNode.next = nextDist
        currentNode = nextDist
    
    return linkedList






