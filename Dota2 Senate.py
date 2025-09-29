class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        ## best strategy: ban whatever opposite parties from the remaining
        idx = {}
        Radiant, Dire = [], []
        for i in range(len(senate)): ## O(N)
            idx[i] = senate[i]
            if senate[i] == "R": Radiant.append(i)
            else: Dire.append(i)

        if Radiant == []: return "Dire"
        elif Dire == []: return "Radiant"
        ## Given that they would remove a party when they can
        ## At the end, it must be one of the list being empty
        ## If remove the begining every time, it will take O(N^2)
        rstart, dstart = 0, 0
        queue = list(range(len(senate)))
        for i in queue:
            if i not in idx:
                continue
            else:
                if senate[i] == "R":
                    del idx[Dire[dstart]]
                    dstart += 1
                    queue.append(i)
                    if dstart >= len(Dire):
                        return "Radiant"
                    ## after it executes, it will be moved to the end
                    Radiant.append(i)
                    rstart += 1
                else:
                    del idx[Radiant[rstart]]
                    rstart += 1
                    queue.append(i)
                    if rstart >= len(Radiant):
                        return "Dire"
                    Dire.append(i)
                    dstart += 1
        
        