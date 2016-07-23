class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #BAcktrace bruteforce: https://discuss.leetcode.com/topic/48001/backtracking-solution/2 
        # refer https://discuss.leetcode.com/topic/48332/java-o-1-with-explanation
        #https://discuss.leetcode.com/topic/47983/java-dp-o-1-solution/2
        if n == 0:
            return 1
        
        n = min(10, n)
        
        count = 9
        totalCount = 10
        for i in range(1, n):
            count *= 10 - i 
            totalCount += count
        return totalCount
            
            
