'''
输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
输出：[[0,0,0],[0,1,0],[0,0,0]]
'''
class solution:
      def process(self,mat):
          visited = set()
          dequeue = []
          m,n = len(mat) , len(mat[0])
          for i in range(m):
              for j in range(n):
                  if mat[i][j] == 0:
                     visited.add((i,j))
                     dequeue.append([i,j])
          while dequeue:
                x,y = dequeue.pop(0)
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    i, j = x + dx, y + dy
                    if 0 <= i < m  and 0 <= j < n and (i,j) not in visited:
                       visited.add((i,j))
                       dequeue.append([i,j])
                       mat[i][j] = mat[x][y] + 1
          return mat
