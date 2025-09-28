class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## read numbers from left and right
        ## gap to record the index of the 0 being deleted
        ## if the current number is 1, then add right by 1
        ## if the current number is 0, but there is no zero before, then add right by 1
        ## if the current number is 0, but there is zero already use, then remove the first zero deleted,
        ## that is, the number of one before gap all removed from current
        ## add right by one, change left to the gap+1, update gap
        left = 0
        gap = None
        current, result = 0, 0
        for i in range(len(nums)):
            num = nums[i]
            if num == 1:
                current += 1
            if num == 0 and gap == None:
                gap = i
            elif num == 0 and gap != None:
                ones = gap - left
                current -= ones
                left = gap + 1
                gap = i
            if result < current:
                result = current
        if gap == None:
            result -= 1
        return result
   