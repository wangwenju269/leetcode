'''
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
'''


class Solution:
    def pacificAtlantic(self, heights) :
        m, n = len(heights), len(heights[0])
        visit_p = [[0] * n for _ in range(m)]
        visit_a = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0 or i == 0:
                   self.dfs(heights, i, j, visit_a)
                if i == m-1 or j == n-1:
                   self.dfs(heights,i,j, visit_p)
        res = []
        for i in range(m):
            for j in range(n):
                if visit_p[i][j] and visit_a[i][j]:
                   res.append([i,j])
        return res



    def dfs(self,heights, i, j, visited):
        m, n = len(heights), len(heights[0])
        visited[i][j] = 1
        for x, y in [(i + 1, j), (i, j + 1),(i-1,j),(i,j-1)]:
            if 0 <= x < m and 0 <= y < n and visited[x][y] == 0:
                if heights[x][y] >= heights[i][j]:
                   self.dfs(heights, x, y, visited)

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(Solution().pacificAtlantic(heights))