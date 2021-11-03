def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1  # high 指针
        else:
            low = mid + 1  # low 指针
    return None


def binary_search_recursion(theList, left, right, target):
    if left > right:
        return None

    midIndex = int((left + right) / 2)
    midValue = theList[midIndex]

    if midValue == target:
        return midIndex

    elif target > midValue:
        return binary_search_recursion(theList, midIndex + 1, right, target)
    else:
        return binary_search_recursion(theList, left, midIndex - 1, target)


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
print(binary_search_recursion(my_list, 0, len(my_list), -1))

