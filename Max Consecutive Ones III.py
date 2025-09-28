class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ## we initialize left and right, keep track of the current index O(N)
        ## every time, we increase right by one (simply keep track length) 
        ## if indexed num == 1, add current by 1
        ## if indexed num == 0, add number of zero by 1
        ## if number of zero is larger than k, add left by one
        ## if the leftest number is 1, reduce current by 1
        left, right = 0, 0
        current, zeros = 0, 0
        result = 0
        for i in range(len(nums)):
            num = nums[i]
            if num == 1: current += 1
            elif num == 0: 
                zeros += 1
                if zeros <= k:
                    current += 1
            if zeros > k: 
                if nums[left] == 1: current -= 1
                else: zeros -= 1
                left += 1
            if current > result:
                result = current
            right += 1
        return result
