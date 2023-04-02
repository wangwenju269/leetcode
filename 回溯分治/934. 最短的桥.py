'''
grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
return 1
'''
class Solution:
    def __init__(self):
        self.temp = set()
        self.flag = False
    def shortestBridge(self, grid) -> int:
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                   self.dfs(i,j,grid)
                   self.flag = True
                   break
            if  self.flag:
                break
        return self.bfs(grid)

    def dfs(self,i,j,grid):
        m, n = len(grid), len(grid[0])
        grid[i][j] = '#'
        for x,y in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
            if 0 <= x < m and 0 <= y < n:
               if grid[x][y] == 1:
                  self.dfs(x,y,grid)
               elif grid[x][y] == 0:
                  self.temp.add((x,y))

    def bfs(self,grid):
        m, n = len(grid), len(grid[0])
        vec = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = list(self.temp)
        count = 1
        while queue:
              for _ in range(len(queue)):
                  i, j = queue.pop(0)
                  for dx, dy in vec:
                      x = i + dx
                      y = j + dy
                      if 0 <= x < m and 0 <= y < n :
                         if  grid[x][y] == 1:
                             return count
                         elif  grid[x][y] == 0:
                             queue.append((x,y))
              count += 1
        return count

grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
print(Solution().shortestBridge(grid))