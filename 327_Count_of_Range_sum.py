class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        #lower < y-current < upper  ==> current+lower <= y <= current+upper
        
        presum=[0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            presum[i] = presum[i-1]+nums[i-1]
        
        def mergeCountRangeSum(sums, start, end, lower, uppper):
            if end-start<=1:
                return 0
            mid = (start+end)/2
            count = mergeCountRangeSum(sums, start, mid, lower, upper)+\
                    mergeCountRangeSum(sums, mid, end, lower, upper)
            
            j = k = mid
            t = mid # for merging sorting two subarray
            i = start
            cache=[0]*(end-start)
            cacheIndex = 0
            while i <mid:
                while j < end and sums[j] < sums[i]+lower:
                    j += 1
                while k < end and sums[k] <= sums[i]+upper:
                    k += 1
                while t < end and sums[t] <= sums[i]:
                    cache[cacheIndex] = sums[t]
                    cacheIndex, t = cacheIndex+1, t+1
                cache[cacheIndex] = sums[i]
                count += k-j
                cacheIndex, i = cacheIndex+1, i+1
            #sums[start:end] = cache[:] Wrong! [2147483647,-2147483648,-1,0]  -1   0, presums=[0,2147483647,-1,-2,-2]
            sums[start:start+cacheIndex] = cache[:cacheIndex]  
            return count
        return mergeCountRangeSum(presum, 0, len(nums)+1, lower, upper)
                
            
"""
Question:
 Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2. 

refer https://discuss.leetcode.com/topic/33738/share-my-solution
"""

# http://huntzhan.org/leetcode-count-of-range-sum/ has multiple solutions
