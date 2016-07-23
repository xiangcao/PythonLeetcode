class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        m, n = len(grid), len(grid[0])
        vectorI, vectorJ =[], []
        def getMinDistance(vector):
            i, j = 0, len(vector)-1
            distance = 0
            while i < j:
                distance += vector[j] - vector[i]
                j -= 1
                i += 1
            return distance
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    vectorI.append(i)
                    

        for j in range(n):
            for i in range(m):
                if grid[i][j]:
                    vectorJ.append(j)
                    
        return  getMinDistance(vectorI) + getMinDistance(vectorJ)
        
