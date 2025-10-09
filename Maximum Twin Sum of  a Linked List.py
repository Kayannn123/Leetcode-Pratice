# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        vals = []
        current = head
        while current != None:
            vals.append(current.val)
            current = current.next
        result = 0
        i = 0
        n = len(vals)
        for i in range(n/2):
            temp = vals[i] + vals[n-1-i]
            if temp > result:
                result = temp
        return result