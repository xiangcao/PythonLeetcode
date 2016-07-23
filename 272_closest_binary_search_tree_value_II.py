"""




"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        pred = []
        successor=[]
        
        def getPredecessor(pred):
            result = pred.pop()
            left = result.left
            while left:
                pred.append(left)
                left = left.right
        
            return result.val
        def getSuccessor(successor):
            result = successor.pop()
            right = result.right
            while right:
                successor.append(right)
                right = right.left
            return result.val

        while root:
            if root.val>target:
                successor.append(root)
                root = root.left
            else:
                pred.append(root)
                root = root.right
        
        result=[]
        while k>0:
            if not pred and not successor:
                break
            elif not pred:
                result.append(getSuccessor(successor))
            elif not successor:
                result.append(getPredecessor(pred))
            else:
                if (abs(successor[-1].val - target) > abs(pred[-1].val-target)):
                    result.append(getPredecessor(pred))
                else:
                    result.append(getSuccessor(successor))
            k -= 1
        return result
            

