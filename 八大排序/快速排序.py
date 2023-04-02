def quick_sort(nums, left, right):
    if left >= right :
       return nums
    i, j = left, right
    base = nums[i]
    while i < j :
          while i < j and nums[j] >= base:
                j -= 1
          while i < j and nums[i] <= base:
                i += 1
          nums[i], nums[j] = nums[j], nums[i]
          if i == j :
             nums[left] = nums[i]
             nums[i] = base
    quick_sort(nums,left, i-1)
    quick_sort(nums,i+1, right)
    return nums
if __name__ == "__main__":
    lists = [56,18, 24, 5, 12, 30, 36, 58, 42, 39]
    print("排序前的序列为：")
    for i in lists:
        print(i, end=" ")
    print("\n排序后的序列为：")
    print(quick_sort(lists, 0, len(lists) - 1))
