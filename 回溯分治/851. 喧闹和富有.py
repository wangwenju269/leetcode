'''
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
'''
from collections import defaultdict
class Solution:
    def loudAndRich(self, richer, quiet):
        graph = defaultdict(list)
        for v, u in richer:
            graph[u].append(v)
        n = len(quiet)
        result = [None] * n
        for i in range(n):
            self.dfs(i, graph,result, quiet)
        return result

    def dfs(self, node, graph,result, quiet):
        if  result[node] == None:
            result[node] = node
            for child in graph[node]:
                    cand = self.dfs(child, graph,result,quiet)
                    if quiet[cand] < quiet[result[node]]:
                       result[node] = cand
        return result[node]


from collections import defaultdict
class solution:
    def loudAndRich(self, richer, quiet):
        graph = defaultdict(list)
        for v, u in richer:
            graph[u].append(v)
        answer = list(range(len(quiet)))
        for i in range(len(quiet)):
            self.dfs(graph, quiet, answer, i)
        return answer

    def dfs(self, graph, quiet, answer, node):
        for child in graph[node]:
                cand = self.dfs(graph, quiet, answer, child)
                if  quiet[cand] < quiet[answer[node]]:
                    answer[node] = cand
        return answer[node]


richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
print(solution().loudAndRich(richer,quiet))