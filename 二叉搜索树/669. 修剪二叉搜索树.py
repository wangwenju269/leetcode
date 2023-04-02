class Solution:
    def trimBST(self, root, low: int, high: int) :
        return self.dfs(root, low, high)

    def dfs(self, root, low, high):
        if not root:
            return None
        elif root.val > high:
            return self.dfs(root.left, low, high)
        elif root.val < low:
            return self.dfs(root.right, low, high)
        else:
            root.left = self.dfs(root.left, low, high)
            root.right = self.dfs(root.right, low, high)
            return root
        