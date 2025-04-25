def linear_search(arr, target):
    """
    Perform a linear search on the array to find the target value.

    :param arr: List of elements to search
    :param target: Value to search for
    :return: Index of the target value if found, otherwise -1
    """

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
    
arr = [10, 20, 30, 40, 50]
target = 30
    
print("Element found at index:", linear_search(arr, target))

        