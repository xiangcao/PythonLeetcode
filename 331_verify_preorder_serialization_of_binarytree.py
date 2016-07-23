class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        
        nodes = preorder.split(",")
        
        diff = 1
        for node in nodes:
            diff -= 1
            if diff < 0: return False
            if node != "#":
                diff += 2
        return diff == 0
       

# refer https://leetcode.com/discuss/83824/7-lines-easy-java-solution 
