class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        #my idea is based on this solution: https://discuss.leetcode.com/topic/31702/36-ms-c-solution/2
        # another good reference is: https://discuss.leetcode.com/topic/31925/java-solution-with-explanation-and-time-complexity-analysis

        grid = copy.deepcopy(grid)
        m, n = len(grid), len(grid[0])
        walk = 0
        totalDistance= [[0]*n for i in range(m)]
        delta=[0,1,0,-1,0]
        def isValid(nextI, nextJ):
            if nextI in range(m) and nextJ in range(n):
                return True
            else:
                return False

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    #BFS. reach all empty lands
                    minDistance = -1
                    queue = collections.deque([(i,j)])
                    level = 1
                    while queue:
                        size = len(queue)
                        for k in range(size):
                            cur = queue.pop()
                            for l in range(4):
                                nextI = cur[0] + delta[l]
                                nextJ = cur[1] + delta[l+1]
                                if isValid(nextI, nextJ) and grid[nextI][nextJ] == walk: # only look at the empty spot which is connected to all previous buildings. 
                                    grid[nextI][nextJ] -= 1
                                    totalDistance[nextI][nextJ] += level
                                    queue.appendleft((nextI, nextJ))
                                    if minDistance < 0 or minDistance > totalDistance[nextI][nextJ]:
                                        minDistance = totalDistance[nextI][nextJ]
                        level += 1
                    walk -= 1
                
        
        return minDistance
        
