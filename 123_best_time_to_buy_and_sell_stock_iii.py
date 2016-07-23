class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        leftMaximum = [0] * n
        rightMaximum = [0] * n
        
        minPrice = prices[0]
        for i in range(1, n):
            minPrice = min(prices[i], minPrice)
            leftMaximum[i] = max(leftMaximum[i-1], prices[i] - minPrice)
        
        maxPrice = prices[n-1]
        for j in range(n-2, -1, -1):
            maxPrice = max(prices[j], maxPrice)
            rightMaximum[j] = max(rightMaximum[j+1], maxPrice - prices[j])
        
        maxProfit = 0
        for i in range(n-1):
            maxProfit = max(maxProfit, leftMaximum[i] + rightMaximum[i+1])

        #maxProfit = max(maxProfit, leftMaximum[n-1], rightMaximum[0]) also works. but can be simplified to below
        maxProfit = max(maxProfit, leftMaximum[n-1])
        return maxProfit
