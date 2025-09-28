class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ## case 1: all same directions 
        ## case 2: left at left, right at right
        ## case 3: left after right - > collisions
        ## if there are left after right -> all left, all right -> stop
        current = []
        for i in range(len(asteroids)): ## O(N)
            ast = asteroids[i]
            if ast > 0: current.append(ast) ## right
            elif current == [] or (current != [] and current[-1] < 0): current.append(ast)
            else:
                ## if it's larger
                ## All right removed / Encounter a larger/equal right
                counter = True
                while current != [] and current[-1] > 0:
                    if abs(ast) < abs(current[-1]): 
                        counter = False
                        break
                    elif abs(ast) == abs(current[-1]): 
                        counter = False
                        current.pop() # remove the last element
                        break
                    else: ## most complicated case
                        current.pop()
                if counter: ## all right removed and there is no larger/equal element
                    current.append(ast)
        ## still O(N), this is because when removed they at most remove O(N)
        return current



