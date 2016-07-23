class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def isMatchHelper(sIndex, pIndex):
            if pIndex == len(p):   return sIndex == len(s)
            
            if sIndex ==  len(s):
                return pIndex == len(p) or (pIndex == len(p)-2 and p[pIndex+1] == '*')
            
            if(pIndex < len(p)-1 and p[pIndex + 1] == '*'):
                return isMatchHelper(sIndex, pIndex+2) or \
                       ((p[pIndex] ==  '.' or p[pIndex] == s[sIndex]) \
                        & isMatchHelper(sIndex+1, pIndex))
            
            else:
                return (p[pIndex] ==  '.' or p[pIndex] == s[sIndex] ) & isMatchHelper(sIndex+1, pIndex+1)

        return isMatchHelper(0,0)
        
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
        
        if len(s) == 0:
            return len(p) <=2 and p[-1] == '*'
    
        if len(p) > 1 and '*' == p[1]:
            return self.isMatch(s, p[2:]) or  ( (p[0] == s[0] or p[0] == '.') and self.isMatch(s[1:], p))
        else:
            return (p[0] == s[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
            
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(s)+1) for i in range(len(p)+1)]
        dp[0][0]= True
        
        #"a"   "ab*a"   False
        # "aa" "a*" True
        
        #s is empty
        for i in range(2, len(p)+1):
            dp[i][0] = p[i-1] == '*' and dp[i-2][0]
            
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == '*':
                    #whether to match p[i-2] with s[j-1] 
                    dp[i][j] = dp[i-2][j] or ((p[i-2] == s[j-1] or p[i-2] == '.') and dp[i][j-1]) #dp[i-2][j-1])
                else:
                    dp[i][j] = (p[i-1] == s[j-1] or p[i-1] == '.') and dp[i-1][j-1]
        return dp[-1][-1]
