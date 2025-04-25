def insert_at(arr, index, value):
    """
    Insert an element into the array at the specified index.

    :param arr: List of elements to insert into
    :param index: Index at which to insert the new element
    :param value: Value to insert
    :return: New list with the new element inserted at the specified index
    """
    if index > len(arr):
        return "Invalid index"
    return arr[:index] + [value] + arr[index:]

arr = [10, 20, 30, 40, 50]
print("Original array:", arr)

new_arr = insert_at(arr, 2, 25)
print("Array after insertion:", new_arr)