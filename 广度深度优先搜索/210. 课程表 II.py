import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites) :
        edges = collections.defaultdict(list)
        degress = [0] * numCourses
        result = []
        for u,  v in prerequisites:
            edges[v].append(u)
            degress[u] += 1
        dequeue = [i for i in range(numCourses) if degress[i] == 0]
        while dequeue:
              node = dequeue.pop(0)
              result.append(node)
              for child in edges[node]:
                  degress[child] -= 1
                  if degress[child] == 0:
                     dequeue.append(child)
        if len(result) != numCourses:
            result = list()
        return result
