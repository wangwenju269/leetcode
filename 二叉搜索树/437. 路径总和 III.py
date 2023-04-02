class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        if not root:
             return 0
        return self.dfs(root,targetSum) + self.pathSum(root.left,targetSum) + self.pathSum(root.right,targetSum)
    def dfs(self,root,targetSum):
          if not root :
             return 0
          count = 0
          if root.val == targetSum:
             count += 1
          count += self.dfs(root.left,  targetSum-root.val)
          count += self.dfs(root.right, targetSum-root.val)
          return count




