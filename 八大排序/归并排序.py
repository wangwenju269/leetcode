def mergeSort(arr):
    # 因为是递归，所以要有个终止条件，这里的终止条件是最终分成1个元素了就返回只有1个元素的列表
    if len(arr) <= 1:
       return arr
    # 将列表分1半，比如11//2结果是5
    middle = len(arr) // 2
    # 切片，分为左边一部分，右边一部分
    left, right = arr[0:middle], arr[middle:]
    # 调用自身函数mergeSort，把左边右边部分传进去，就会继续按照上面代码分成2部分
    # merge函数是用来排序的，并且将排序好的元素放到了新的列表里
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    # 新排序的放到result里
    result = []
    # 当左右两个类标里都有元素时,进行循环
    while left and right:
        # 如果左列表的第1个元素 <= 列表里的第1个元素
        if left[0] <= right[0]:
            # 把左列表的第1个元素用pop函数提取出来，加到新的列表里
            result.append(left.pop(0))
        else:
            # 否则就把右列表的第1个元素提取出来，加到新的列表里
            result.append(right.pop(0))

    # 上面循环后，可能某个列表里还有元素，所以继续下面的操作，有的话，直接依次加到新的列表里即可，因为剩下的元素肯定是比已经比较完的大的
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

seq = [5, 3, 0, 6, 1, 4]
result = mergeSort(seq)
print(result)