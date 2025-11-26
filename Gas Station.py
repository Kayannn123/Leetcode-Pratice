class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost): return -1
        gas = deque(gas)
        cost = deque(cost)
        n = len(gas)
        idx, cur, counter, progress = None, 0, 0, 0
        while progress < n: ##not finished
            curgas = gas.popleft()
            curcost = cost.popleft()
            if idx != None:
                cur += curgas - curcost
                progress += 1
            elif curgas >= curcost:
                idx = counter
                cur += curgas - curcost
                progress += 1
            if cur < 0:
                idx = None
                progress = 0
                cur = 0
            gas.append(curgas)
            cost.append(curcost)
            counter += 1
            counter = counter % n
        return idx
