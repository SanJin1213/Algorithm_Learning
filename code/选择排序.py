def findSmallest(arr):
    smallest = arr[0]
    # 取列表中第一个值
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# 使用选择排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


sel = selectionSort([5, 3, 6, 2, 10])
print(sel)

# 一直循环到arr列表中没有元素
# 每次都是筛选出arr中最小的值
