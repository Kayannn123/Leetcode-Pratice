# Definition for singly-linked list.
import math

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ## keep a record of index
        idx = {}
        i = 0
        node = head
        while node != None:
            idx[i] = node
            node = node.next
            i += 1
        x = math.floor(len(idx)/2)
        if len(idx) == 1: return None
        elif len(idx) == 2: 
            idx[0].next = None
            return idx[0]
        left = idx[x-1]
        right = idx[x+1]
        left.next = right
        return idx[0]