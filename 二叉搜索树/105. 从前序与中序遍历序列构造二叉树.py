'''
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7
'''
'''
解题思路：
先序遍历：中左右
中序遍历：左中右
'''
class TreeNode:
      def __init__(self,val,left = None, right = None):
          self.val = val
          self.left = left
          self.right = right
class BuildTree:
      def build_tree(self,preorder,inorder):
          if not preorder:
             return None
          val = preorder.pop(0)
          root = TreeNode(val)
          i = inorder.index(val)
          root.left = self.build_tree(preorder[:i],inorder[:i])
          root.right = self.build_tree(preorder[i:],inorder[i+1:])
          return root
      