# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        def helper(parent, root, length):
            if not root:
                return length
            if root.val-parent.val == 1:
                length += 1
            else:
                length = 1
            length = max(length, helper(root, root.left, length), helper(root, root.right, length))
            
            """
            wrong code: find what is the bug? 
            length = max(length, helper(root, root.left, length))
            length = max(length, helper(root, root.right, length))
            """

            return length

        length = max( helper(root, root.left, 1), helper(root, root.right, 1))
        return length
