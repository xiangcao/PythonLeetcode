class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.strip()
        
        # "+, -" : 0
        # "digit": 1
        # "dot": 2
        # "e":3
        transitionTable=[[1,2,3,-1],[-1,2,3,-1],[-1,2,3,5],[-1,4,-1,5],[-1,4,-1,5],[6,7,-1,-1],[-1,7,-1,-1],[-1,7,-1,-1]]
        
        state = 0
        flag = 0
        for i in s:
            input = -1
            if  i >= '0' and i<='9':
                flag = 1
                input = 1
            elif i == '+' or i == '-':
                input = 0
            elif i == '.':
                input = 2
            elif i == 'e':
                input = 3
            
            if input == -1:
                return False
            if state == 3 and input == 3:
                state = 5 if flag else -1 
            else:
                state = transitionTable[state][input]
            if state == -1:
                return False
        return state ==2 or (flag and state== 3) or state== 4 or state== 7
            
                
# refer https://discuss.leetcode.com/topic/4219/c-my-thought-with-dfa
# refer https://discuss.leetcode.com/topic/30058/a-simple-solution-in-python-based-on-dfa


