'''
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
'''
### dfs 搜索解
from collections import defaultdict
class Solution:
    def __init__(self):
        self.flag = True
    def canFinish(self, numCourses, prerequisites) :
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)
        visited = [0] * numCourses
        for i in range(numCourses):
            if visited[i] == 0:
               self.dfs(i,graph,visited)
        return self.flag

    def dfs(self,i,graph,visited):
        visited[i] = 1
        for j in graph[i]:
            if visited[j] == 0:
               self.dfs(j,graph,visited)
            elif visited[j] == 1:
               self.flag = False
               return
        visited[i] = 2

### bfs 解

class solution:

    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        degree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            degree[u] += 1
        ''' 叶子节点入度的数量值为0 '''
        dequeue = [i for i in range(numCourses) if degree[i] == 0]
        '''返回BOOL的条件是：'''
        count = 0
        while dequeue:
              count += 1
              node = degree.pop(0)
              for child in graph[node]:
                  degree[child] -= 1
                  if degree[child] == 0:
                      dequeue.append(child)
        return count == numCourses


