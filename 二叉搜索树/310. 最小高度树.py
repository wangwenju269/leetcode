from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges) :
        if n == 1:
           return [0]
        graph = defaultdict(list)
        for u ,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue = [u for u in range(n) if len(graph[u]) == 1]
        print(queue)
        while n > 2:
              n -= len(queue)
              for _ in range(len(queue)):
                  node = queue.pop(0)
                  for child in graph[node]:
                        graph[child].remove(node)
                        if len(graph[child]) == 1:
                           queue.append(child)
        return queue

from collections import defaultdict
class solution:
    def findMinHeightTrees(self, n: int, edges) :
        if n == 1:
           return [0]
        graph = defaultdict(list)
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dequeue = [u for u in range(n) if len(graph[u]) == 1]
        print(dequeue)
        while n > 2:
                n -= len(dequeue)
                for _ in range(len(dequeue)):
                    node = dequeue.pop(0)
                    for child  in graph[node]:
                        graph[child].remove(node)
                        if len(graph[child]) == 1:
                           dequeue.append(child)
        return dequeue

n = 6
edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]
print(Solution().findMinHeightTrees(n,edges))