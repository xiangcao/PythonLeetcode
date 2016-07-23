class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #merge sort, stable sorting
        
        smaller=[0]*len(nums)
        def mergeCountSmaller(enum):
            if len(enum)<=1:
                return enum
            else:
                mid = len(enum)/2
                left, right = mergeCountSmaller(enum[:mid]), mergeCountSmaller(enum[mid:])
                for i in range(len(enum)-1, -1, -1):
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        mergeCountSmaller(list(enumerate(nums)))
        return smaller
       
"""
https://discuss.leetcode.com/topic/31162/mergesort-solution/2

 The smaller numbers on the right of a number are exactly those that jump from its right to its left during a stable sort. So I do mergesort with added tracking of those right-to-left jumps.

"""


"""
https://discuss.leetcode.com/topic/31288/c-o-nlogn-time-o-n-space-mergesort-solution-with-detail-explanation/2
"""
