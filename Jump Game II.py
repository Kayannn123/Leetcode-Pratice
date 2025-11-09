class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## for the range of each step, select the farthest
        ## record the last step and move to next range
        current = 0 
        count = 0
        while current < len(nums) - 1:
            steps = nums[current]
            counter = current
            temp = current
            for i in range(temp+1, temp+steps+1):
                if i >= len(nums)-1: 
                    return count+1
                farther = i + nums[i]
                if counter < farther:
                    counter = farther
                    current = i
            count += 1
        return count
        