def heap_sink(heap, heap_size, parent_index):
    """最大堆-下沉算法"""
    child_index = 2 * parent_index + 1

    # temp保存需要下沉的父节点，用于最后赋值
    temp = heap[parent_index]

    while child_index < heap_size:
        # 如果有右孩子，且右孩子比左孩子大，则定位到右孩子
        if child_index + 1 < heap_size and heap[child_index + 1] > heap[child_index]:
            child_index += 1

        # 如果父节点的值不小于左右孩子节点的值，可直接跳出循环
        if temp >= heap[child_index]:
            break

        heap[parent_index] = heap[child_index]
        parent_index = child_index
        child_index = 2 * parent_index + 1

    heap[parent_index] = temp


def heap_sort(mylist):
    """堆排序"""
    n = len(mylist)

    # 1. 无序列表构建成最大堆
    for i in range(n - 2 // 2, -1, -1):
        heap_sink(mylist, n, i)

    # 2. 循环删除堆顶元素，移到列表尾部，调节堆产生新的堆顶
    for i in range(n - 1, 0, -1):
        mylist[0], mylist[i] = mylist[i], mylist[0]
        heap_sink(mylist, i, 0)


if __name__ == "__main__":
    mylist = [1, 3, 4, 5, 2, 6, 9, 7]
    heap_sort(mylist)
    print(mylist)