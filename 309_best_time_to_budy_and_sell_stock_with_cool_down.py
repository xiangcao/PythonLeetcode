class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # https://discuss.leetcode.com/topic/30680/share-my-dp-solution-by-state-machine-thinking
        # https://discuss.leetcode.com/topic/30421/share-my-thinking-process
        n = len(prices)
        if n == 0:
            return 0
        buyEnding = [0] * n
        restEnding = [0] * n
        sellEnding = [0] * n
        buyEnding[0] = -prices[0]
        restEnding[0] = 0
        sellEnding[0] = 0
        for i in range(1,n):
            buyEnding[i] = max(buyEnding[i-1], restEnding[i-1]-prices[i])
            restEnding[i] = sellEnding[i-1]
            sellEnding[i] = max(sellEnding[i-1], buyEnding[i-1]+prices[i])
        
        return sellEnding[n-1]
        #buy, prev_buy, sell, prev_sell
        
