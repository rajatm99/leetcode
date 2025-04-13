from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.leaf1 = []
        self.leaf2 = []

    def dfs(self, tree, root):
        if root == None:
            return
        if root.left == None and root.right == None:
            self.leaf1.append(root.val) if tree == "1" else self.leaf2.append(root.val)

        self.dfs(tree, root.left)
        self.dfs(tree, root.right)
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.dfs("1", root1)
        self.dfs("2", root2)

        print(self.leaf1)
        print(self.leaf2)    

        if len(self.leaf1) != len(self.leaf2):
            return False

        i = 0
        while i < len(self.leaf1):
            if self.leaf1[i] != self.leaf2[i]:
                return False
            i += 1
        return True   