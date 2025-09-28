class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ## with left and right, move the one with lower to check if any improvement
        result = 0
        left = 0
        right = len(height)-1
        while left < right:
            lower = min(height[left], height[right])
            counter = lower*(right - left)
            if counter > result: result = counter
            if height[left] == lower:
                left += 1
            elif height[right] == lower:
                right -= 1
        return result
