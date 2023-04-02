class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = self.dfs(i, j, grid)
                    ans = max(ans, count)
        return ans

    def dfs(self, i, j, grid):
        m, n = len(grid), len(grid[0])
        grid[i][j] = 0
        count = 1
        vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in vec:
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                count += self.dfs(x, y, grid)
        return count