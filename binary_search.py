def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        current = list[mid]
        if current == item:
            return mid
        if current > item:
            high = mid - 1  # high 指针
        else:
            low = mid + 1  # low 指针
    return None


def binary_search_recursion(list, left, right, target):
    if left > right:
        return None

    midIndex = int((left + right) / 2)
    midValue = list[midIndex]

    if midValue == target:
        return midIndex

    elif target > midValue:
        return binary_search_recursion(list, midIndex + 1, right, target)
    else:
        return binary_search_recursion(list, left, midIndex - 1, target)


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
print(binary_search_recursion(my_list, 0, len(my_list), -1))

