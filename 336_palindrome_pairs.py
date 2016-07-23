class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPalindrome(input):
            left, right = 0, len(input)-1
            while left < right:
                if input[left] == input[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        result=[]
        if len(words) < 2:
            return result
        table={}
        for i in range(len(words)):
            table[words[i]] = i
        
        for i in range(len(words)):
            for j in range(len(words[i])+1):
                str1 = words[i][:j]
                str2 = words[i][j:]
                
                if isPalindrome(str1):
                    candidate = str2[::-1]
                    if candidate in table and table[candidate] != i:
                        result.append([table[candidate], i])
                if isPalindrome(str2) and len(str2) != 0:
                    candidate = str1[::-1] 
                    if candidate in table and table[candidate] != i:
                        result.append([i, table[candidate]])
                        
        return result
