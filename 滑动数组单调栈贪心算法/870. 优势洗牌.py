'''
给定两个大小相等的数组 nums1 和 nums2，nums1 相对于 nums2 的优势可以用满足 nums1[i] > nums2[i] 的索引 i 的数目来描述。
'''
'''
输入：nums1 = [2,7,11,15], nums2 = [1,10,4,11]
输出：[2,11,7,15]
'''
from collections import defaultdict
class solution:
      def process(self,nums1,nums2):
          nums1_copy = sorted(nums1)
          nums2_copy = sorted(nums2)
          graph = defaultdict(list)
          res = []
          i = 0
          for j in range(len(nums1)):
              if nums1_copy[j] > nums2_copy[i]:
                 graph[nums2_copy[i]].append(nums1_copy[j])
                 i += 1
              else:
                 res.append(nums1_copy[i])
          ans = []
          for num in nums2:
              if graph[num]:
                 ret = graph[num].pop()
                 ans.append(ret)
              else:
                 ans.append(res.pop())
          return ans
