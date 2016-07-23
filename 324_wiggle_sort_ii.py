class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # the reason the same exchange method for wiggle sort I does not work here is, when nums[i] == nums[i+1], we can't restore the order by simply exchange nums[i] and nums[i+1]
        """
        for i in range(len(nums)-1):
            if (nums[i] <= nums[i+1] and i % 2 == 1) or (nums[i] >= nums[i+1] and i % 2 == 0):
                nums[i], nums[i+1] = nums[i+1], nums[i]
                
Input: [1,2,2,1,2,1,1,1,1,2,2,2]
Output: [1,2,1,2,1,2,1,1,1,2,2,2]
Expected: [1,2,1,2,1,2,1,2,1,2,1,2] 

        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        # refer https://discuss.leetcode.com/topic/32861/3-lines-python-with-explanation-proof
        
    
    # refer https://discuss.leetcode.com/topic/32929/o-n-o-1-after-median-virtual-indexing
    # refer https://discuss.leetcode.com/topic/32893/o-n-time-and-cheating-o-1-space-solution-will-there-be-a-real-o-1-solution/2?show=77054            
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 1. get the median;  quick select
        def selectKth(nums, k):
            i, j = 0, len(nums)-1
            while i < j:
                m = pivot(nums, i, j )
                length = m-i+1
                if length == k:
                    return nums[m]
                elif length < k:
                    i = m+1
                    k -= length
                else:
                    j = m-1
                
            return nums[i] # only in the case k become 1 and i become the median element itself will we come to this point
            
        def pivot(nums, i, j):
            nums[i], nums[(i+j)/2] = nums[(i+j)/2], nums[i]
            idx = i  #pivot index
            i += 1
            val = nums[idx]
            
            while i < j:
                if nums[i] <= val: 
                    i += 1
                elif nums[j] >= val:
                    j -= 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
            if nums[i] > val:
                i -= 1
            #if nums[i] != nums[idx]:
            nums[i], nums[idx] = nums[idx], nums[i]
            return i
            
        def getMedian(nums):
            if len(nums) % 2 == 1:
                return selectKth(nums,len(nums)/2+1)
            else:
                return (selectKth(nums,len(nums)/2) + selectKth(nums,len(nums)/2+1)) /2.0
                
        median = getMedian(nums)
        print "median : %s" %median
        # 2. partition the nums, [larger, median, smaller]
        
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        def mapIndex(i):
            return (2*i+1)% (len(nums)  | 1)
        i, j = 0, len(nums)-1
        k = 0
        while k <= j:
            # any element in nums[i:k] must be median
            if nums[mapIndex(k)]>median:
                swap(nums, mapIndex(i), mapIndex(k))
                i += 1 
                k += 1
            elif nums[mapIndex(k)] < median:
                swap(nums, mapIndex(j), mapIndex(k)) # we don't know what value nums[j] may have. thus don't change k here. 
                j -= 1
            else:
                k += 1
        
        
            
            
            
        
       
        
        
