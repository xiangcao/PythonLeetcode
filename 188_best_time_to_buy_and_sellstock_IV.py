class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/26169/clean-java-dp-solution-with-comment/2
        # https://discuss.leetcode.com/topic/9522/c-solution-with-o-n-klgn-time-using-max-heap-and-stack/2
        # https://discuss.leetcode.com/topic/8984/a-concise-dp-solution-in-java/8 
        n = len(prices)
        if n <= 1:
            return 0
        if k > n/2:
            maxPro = 0
            for i in range(1, len(prices)):
                maxPro += max(prices[i]-prices[i-1], 0)
            return maxPro
        
        dp = [[0 for i in range(n)] for j in range(k+1)]
        
        for i in range(1, k+1):
            localMax = dp[i-1][0]-prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + localMax)
                localMax = max(localMax, dp[i-1][j]-prices[j])

        return dp[k][n-1]
                    
            
