class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        visited = [0 for i in range(10)]
        skiptable = [[0 for i in range(10)] for j in range(10)]
        
        skiptable[1][3] = skiptable[3][1] = 2
        skiptable[1][7] = skiptable[7][1] = 4
        skiptable[7][9] = skiptable[9][7] = 8
        skiptable[3][9] = skiptable[9][3] = 6
        skiptable[1][9] = skiptable[9][1] = skiptable[3][7] = skiptable[7][3] \
                        = skiptable[4][6] = skiptable[6][4] = skiptable[2][8] = skiptable[8][2] = 5

        def dfs(i, visited, steps):
            if steps < 0:
                return 0
            if steps == 0:
                return 1
            count = 0
            visited[i] = 1
            for j in range(1,10):
                if visited[j] == 0 and (skiptable[i][j] == 0 or visited[skiptable[i][j]] == 1):
                    count += dfs(j, visited, steps-1)
            visited[i] = 0
            return count
        
        totalcount = 0
        
        for steps in range(m, n+1):
            totalcount += dfs(1, visited, steps-1) * 4
            totalcount += dfs(2, visited, steps-1) * 4
            totalcount += dfs(5, visited, steps-1)
        return totalcount
            
            
