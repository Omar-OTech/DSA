def insert_at(arr, index, value):
    if index > len(arr):
        return "Invalid index"
    return arr[:index] + [value] + arr[index:]

arr = [10, 20, 30, 40, 50]
print("Original array:", arr)

new_arr = insert_at(arr, 2, 25)
print("Array after insertion:", new_arr)