# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        if not root:
            return result
        curLevel = collections.deque([root])
        while curLevel:
            result.append(curLevel[-1].val)
            nextLevel= collections.deque([])
            while curLevel:
                node = curLevel.popleft()
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            curLevel = nextLevel
        return result
                
                
            
