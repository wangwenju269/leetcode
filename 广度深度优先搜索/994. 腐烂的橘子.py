class Solution:
    def __init__(self):
        self.bad = []

    def orangesRotting(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    self.bad.append((i, j))
        dequeue = self.bad
        count = 0
        while dequeue:
            stack = []
            for _ in range(len(dequeue)):
                i, j = dequeue.pop(0)
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n:
                        if grid[x][y] == 1:
                            grid[x][y] = 2
                            stack.append((x, y))
            if stack:
               count += 1
            dequeue = stack

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return count
grid =  [[0]]
print(Solution().orangesRotting(grid))