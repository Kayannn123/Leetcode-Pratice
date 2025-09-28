class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = max(nums) + 1
        j = max(nums) + 1
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        return False
    
