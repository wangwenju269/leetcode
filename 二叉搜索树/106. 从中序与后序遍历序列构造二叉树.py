'''
输入: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
'''
'''
解题思路：
先序遍历：中左右
中序遍历：左中右
后序遍历：左右中
'''
class TreeNode:
      def __init__(self,val,left = None, right = None):
          self.val = val
          self.left = left
          self.right = right
class BuildTree:
      def build_tree(self,inorder,postorder):
          if not postorder:
             return None
          val = postorder.pop()
          root = TreeNode(val)
          i = inorder.index(val)
          root.left = self.build_tree(inorder[:i],postorder[:i])
          root.right = self.build_tree(inorder[i+1:],postorder[i:])
          return root