class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len = 0 
        
        nums = set(nums)
        
        maxlen = 0
        for n in nums:
            if n-1 not in nums:
                m = n+1
                while m in nums:
                    m += 1
                maxlen = max(maxlen, m-n)

        return maxlen
                
"""
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, bool> used;
        for(int i : nums) used[i] = false;
        int maxLen = 0 ;
        for(int i = 0; i < nums.size(); ++i){
            if(used[nums[i]]){
                continue;
            }else{
                used[nums[i]] = true;
                int len = 1;
                int j = nums[i] + 1;
                while(used.find(j) != used.end()){
                    ++len;
                    used[j] = true;
                    ++j;
                }
                j = nums[i] - 1; 
                while(used.find(j) != used.end()){
                    ++len;
                    used[j] = true;
                    --j;
                }
                maxLen = max(maxLen, len);
            }
        }
        return maxLen;
    }
};
"""
        

