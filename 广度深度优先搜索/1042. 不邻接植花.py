from collections import defaultdict
class Solution:
    def gardenNoAdj(self, N: int, paths):
        graph = defaultdict(list)
        for path in paths:
            x0, y0 = path[0], path[1]
            graph[x0].append(y0)
            graph[y0].append(x0)

        res = [0] *(N+1)
        for i in range(1,N+1):
            if i not in graph.keys():
                res[i] = 1
            else:
                opt = [1,2,3,4]
                for neigh in graph[i]:
                    if res[neigh] in opt:
                       opt.remove(res[neigh])
                res[i] = opt[0]
        return res[1:]
n = 4
paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
print(Solution().gardenNoAdj(n,paths))