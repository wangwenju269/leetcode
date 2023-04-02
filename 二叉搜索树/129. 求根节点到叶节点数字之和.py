class Solution:
    def sumNumbers(self, root) -> int:
        if not root:
           return 0
        ans = []
        path = []
        self.dfs(root,path,ans)
        print(ans)
        return sum(map(lambda x:int(''.join([str(i) for i in x])),ans))
    def dfs(self,root,path,ans):
        if  not root:
            return
        if not root.left and not root.right:
            path.append(root.val)
            ans.append(path[:])
            return
        self.dfs(root.left,  path+[root.val],ans)
        self.dfs(root.right, path+[root.val],ans)