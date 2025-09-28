class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = {}
        for i in range(len(grid)):
            if tuple(grid[i]) not in count:
                count[tuple(grid[i])] = 1
            else:
                count[tuple(grid[i])] += 1
        result = 0
        for i in range(len(grid)):
            current = []
            for j in range(len(grid)):
                current.append(grid[j][i])
            if tuple(current) in count:
                result += count[tuple(current)]
        return result