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
    def __init__(self):
        self.ans = 0
    def longestUnivaluePath(self, root) -> int:
        if not root:
           return 0
        self.dfs(root)
        return self.ans

    def dfs(self,root):
        if not root:
           return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        pl, pr = 0, 0
        if root.left and root.val == root.left.val:
           pl = left + 1
        if root.right and root.val == root.right.val:
           pr = right + 1
        self.ans = max(self.ans, pl+ pr + 1)
        return max(pl,pr)







root = [1,4,5,4,4,None,5]
tree = Tree()
tree.nums_bitree(root)

print(Solution().longestUnivaluePath(tree.root))