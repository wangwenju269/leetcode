class Node:
      def __init__(self,val,left = None,right = None):
          self.val = val
          self.left = left
          self.right = right
class Tree:
      def __init__(self):
          self.root = None
      def nums_bitree(self,nums):
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
                      node.right =  Node(nums[i+1]) if nums[i+1] is not None else None
                      dequeue.append(node.right)
                      i += 1
                   i += 1

class Solution:
    def levelOrderBottom(self, root) :
        if not root:
           return []
        dequeue = [root]
        ans = []
        while dequeue:
              stack = []
              for _ in range(len(dequeue)):
                  node = dequeue.pop(0)
                  if node:
                     stack.append(node.val)
                  if node.left:
                      dequeue.append(node.left)
                  if node.right:
                      dequeue.append(node.right)
              ans.append(stack)
        return ans[::-1]



root = [3,9,20,None,None,15,7]
tree = Tree()
tree.nums_bitree(root)

print(Solution().levelOrderBottom(tree.root))