class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        forcandies = [1]*n
        backcandies = [1]*n
        for i in range(1, n):
            temp = ratings[i]
            if ratings[i-1] < temp:
                forcandies[i] = forcandies[i-1]+1
        for i in range(n-2, -1, -1):
            temp = ratings[i]
            if ratings[i+1] < temp:
                backcandies[i] = backcandies[i+1]+1
        candies = [1]*n
        for i in range(n):
            candies[i] = max(backcandies[i], forcandies[i])
        return sum(candies)
