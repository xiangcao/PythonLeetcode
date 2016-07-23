class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result=[]
        def helper(result, pos, path, val, prev):
            if pos == len(num):
                if val == target:
                    result.append(path)
                    return
            for i in range(pos+1, len(num)+1):
                if i > pos+1 and num[pos] == '0': break
                cur = num[pos:i]
                if pos == 0:
                    helper(result, i, path+cur, int(cur), int(cur))
                    continue
                helper(result, i, path+"+"+cur, val+int(cur), int(cur))
                helper(result, i, path+"-"+cur, val-int(cur), -int(cur))
                helper(result, i, path+"*"+cur, val-prev+prev*int(cur), prev*int(cur))
        helper(result, 0, "", 0, 0)
        return result
            
