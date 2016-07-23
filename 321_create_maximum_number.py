class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        def merge(nums1, nums2):
            ans=[]
            while nums1 or nums2:
                if nums1>nums2:
                    ans.append(nums1.pop(0))
                else:
                    ans.append(nums2.pop(0))
            return ans
        
        def getMaxArray(nums, k):
            """
            get max length k subarray 
            """
            n = len(nums)
            ans=[]
            
            maxlocal = -1
            while k:
                maxlocal += 1
                for i in range(maxlocal, n-k+1):
                    if nums[i] > nums[maxlocal]:
                        maxlocal = i
                ans.append(nums[maxlocal])
                k -= 1
            return ans
        
        res = [0]*k
        for i in range(k+1):
            j = k-i
            if i > len(nums1) or j > len(nums2): continue
            res = max(res, merge(getMaxArray(nums1, i), getMaxArray(nums2, j)))
        return res
                    
                

#refer https://discuss.leetcode.com/topic/32281/share-my-python-solution-with-explanation/2
#refer https://discuss.leetcode.com/topic/32272/share-my-greedy-solution/2
#refer https://discuss.leetcode.com/topic/32298/short-python-ruby-c
