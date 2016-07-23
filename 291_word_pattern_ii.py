"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Examples:

    pattern = "abab", str = "redblueredblue" should return true.
    pattern = "aaaa", str = "asdasdasdasd" should return true.
    pattern = "aabb", str = "xyzabcxzyabc" should return false.

Notes:
You may assume both pattern and str contains only lowercase letters. 
"""

class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lettermapping={}
        strmapping={}
        patternlen = len(pattern)
        strlen = len(str)
        
        def dfs(pIndex, strIndex):
            if pIndex == patternlen and strIndex == strlen:
                return True
            if pIndex == patternlen or strIndex == strlen:
                return False
            if pattern[pIndex] in lettermapping:
                mappedStr = lettermapping[pattern[pIndex]]
                if str[strIndex:strIndex+len(mappedStr)] != mappedStr:
                    return False
                else:
                    return dfs(pIndex+1, strIndex+len(mappedStr))
            for ending in range(strIndex+1, strlen- (patternlen-pIndex-1)+1):
                substring = str[strIndex:ending]
                if substring in strmapping:
                    continue
                lettermapping[pattern[pIndex]] = substring
                strmapping[substring] = pattern[pIndex]
                if dfs(pIndex+1, ending):
                    return True
                lettermapping.pop(pattern[pIndex])
                strmapping.pop(substring)
            return False
        return dfs(0, 0)
            
