from collections import defaultdict
class Solution:
    def pyramidTransition(self, bottom: str, allowed):
        graph = defaultdict(list)
        for allow in allowed:
            graph[allow[:-1]].append(allow[-1])
        new_bottom = ''
        return self.dfs(bottom,new_bottom,1,graph)


    def dfs(self,bottom,new_bottom,i, graph):
        if i == len(bottom) :
           if  i == 1:
               return True
           else:
               return self.dfs(new_bottom,'',1,graph)
        new = bottom[i-1:i+1]
        for node in graph[new]:
            if self.dfs(bottom,new_bottom + node,i+1,graph):
               return True
        return False

class solution:
    def pyramidTransition(self, bottom: str, allowed):
        temp = defaultdict(list)
        for sp in allowed:
            temp[sp[0:-1]].append(sp[-1])
        def traceback(s,old,new):
            if  len(new) == len(old)-1:
                if len(new) == 1:
                    return True
                else:
                    return traceback(1,new,'')
            trick = old[s-1:s+1]
            for sp in temp[trick]:
                if traceback(s+1,old,new + sp):
                   return True
            return False
        return traceback(1,bottom,'')

bottom = "BCD"
allowed = ["BCC","CDE","CEA","FFF"]
# print(Solution().pyramidTransition(bottom,allowed))
print(solution().pyramidTransition(bottom,allowed))