class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss = 1
        index = 0
        added = 0
        while miss <= n:
            if index < len(nums) and nums[index] <= miss:
                miss += nums[index]
                index += 1
            else:
                miss += miss
                added += 1
        return added


# https://discuss.leetcode.com/topic/35709/share-my-thinking-process/6
# https://discuss.leetcode.com/topic/35494/solution-explanation
