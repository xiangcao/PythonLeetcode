class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        
        m = len(grid)
        n = 0 if m == 0 else len(grid[0])
        
        result, rowHits, colHits=0, 0, [0]*n
        for i in range(m):
            for j in range(n):
                if not j or grid[i][j-1] == 'W':
                    rowHits = 0
                    k = j
                    while k < n and grid[i][k] != 'W':
                        rowHits += grid[i][k] == 'E'
                        k += 1
                if not i or grid[i-1][j] == 'W':
                    colHits[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        colHits[j] += grid[k][j] == 'E'
                        k += 1
                if grid[i][j] == '0':
                    result = max(result, rowHits + colHits[j])
        return result
        
        
    def maxKilledEnemies(self, grid):
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        result = 0
        colhits = [0] * n
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if j == 0 or row[j-1] == 'W':
                    rowhits = 0
                    k = j
                    while k < n and row[k] != 'W':
                        rowhits += row[k] == 'E'
                        k += 1
                if i == 0 or grid[i-1][j] == 'W':
                    colhits[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        colhits[j] += grid[k][j] == 'E'
                        k += 1
                if cell == '0':
                    result = max(result, rowhits + colhits[j])
        return result

    #totally in-comprehensible by StefanPochmann
    # https://leetcode.com/discuss/109117/short-o-mn-python 
    def maxKilledEnemies(self, grid):
        def hits(grid):
            return [[h
                     for block in ''.join(row).split('W')
                     for h in [block.count('E')] * len(block) + [0]]
                    for row in grid]
        rowhits = hits(grid)
        colhits = zip(*hits(zip(*grid)))
        return max([rh + ch
                    for row in zip(grid, rowhits, colhits)
                    for cell, rh, ch in zip(*row)
                    if cell == '0'] or [0])
