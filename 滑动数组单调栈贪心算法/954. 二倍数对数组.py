'''
arr = [4,-2,2,-4]
'''
from collections import Counter
'''哈希映射解题思想'''
def process(arr):
    hash_map = Counter(arr)
    arr.sort(key = abs)
    for num in arr:
        if hash_map[num] == 0:
           continue
        if hash_map[num * 2] == 0:
           return False
        else:
           hash_map[num * 2] -= 1
           hash_map[num] -= 1
    return True

arr = [1,2,1,-8,8,-4,4,-4,2,-2]
print(process(arr))