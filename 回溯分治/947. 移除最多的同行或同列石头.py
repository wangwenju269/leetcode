class Solution:
    def removeStones(self, stones):
        res = set()
        uf = unionfind()
        for x,y in stones:
            uf.union(x,y+10001)
        # print(uf.parent)
        for i, j in stones:
            res.add(uf.find(i))
        return len(stones)- len(res)

class unionfind:
      def __init__(self):
          self.parent = {}

      def union(self,id1,id2):
          self.parent[self.find(id1)] = self.find(id2)

      def find(self,id):
          if id not in self.parent:
              self.parent[id] = id
          if id != self.parent[id]:
             self.parent[id] = self.find(self.parent[id])
          return self.parent[id]