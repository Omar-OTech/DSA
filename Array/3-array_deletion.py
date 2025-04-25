def delete_at(arr, index):
    if index >= len(arr):
        return "Invalid index"
    return arr[:index] + arr[index+1:]

arr = [10, 20, 25, 30, 40, 50]
print("Original array:", arr)

new_arr = delete_at(arr, 2)
print("Array after deletion:", new_arr)
