class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def nums_bitree(self, nums):
        if not nums:
            return None
        self.root = Node(nums[0])
        dequeue = [self.root]
        n = len(nums)
        i = 1
        while i < n:
            node = dequeue.pop(0)
            if node:
                node.left = Node(nums[i]) if nums[i] is not None else None
                dequeue.append(node.left)
                if i + 1 < n:
                    node.right = Node(nums[i + 1]) if nums[i + 1] is not None else None
                    dequeue.append(node.right)
                    i += 1
                i += 1

class Solution:
    def pathSum(self, root, targetSum: int):
        if not root:
           return []
        path = []
        ans = []
        self.dfs(root,targetSum,path,ans)
        return ans
    def dfs(self,root,targetSum,path,ans):
        if not root:
           return None
        targetSum -= root.val
        if targetSum == 0 and not root.left and not root.right:
           path += [root.val]
           ans.append(path[:])
           return
        self.dfs(root.left, targetSum,path+[root.val],ans)
        self.dfs(root.right,targetSum,path+[root.val],ans)



root = [5,4,8,11,None,13,4,7,2,None,None,5,1]
targetSum = 22
tree = Tree()
tree.nums_bitree(root)
print(Solution().pathSum(tree.root,targetSum))