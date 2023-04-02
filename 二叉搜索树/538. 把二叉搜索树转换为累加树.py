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
    def convertBST(self, root):
        if not root:
            return None
        return self.dfs(root)
    '''右中左遍历'''
    def dfs(self,root):
        if not root:
            return
        self.dfs(root.right)
        root.val += self.ans
        self.ans = root.val
        self.dfs(root.left)
        return root

root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
tree = Tree()
tree.nums_bitree(root)
print(Solution().convertBST(tree.root))