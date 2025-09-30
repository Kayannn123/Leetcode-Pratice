# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ## keep track of the last item of odd and the first item of even
        ## keep track of the current item of even
        if head == None or head.next == None: return head
        even, odd = head.next, head
        current = even
        turn = "odd"
        node = even.next
        while node != None:
            if turn == "odd":
                odd.next = node
                odd = odd.next ## last of odd, never be none
                turn = "even"
            elif turn == "even":
                current.next = node
                turn = "odd"
                current = current.next
            node = node.next
        current.next = None
        odd.next = even
        return head