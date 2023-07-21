def rotate_array_inplace(arr, rotations):
    n = len(arr)
    rotations %= n

    # Reverse the entire array
    start, end = 0, n - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    # Reverse the first part of the array
    start, end = 0, rotations - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    # Reverse the second part of the array
    start, end = rotations, n - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


arr = [1, 2, 3, 4, 5]
rotations = 2
result = rotate_array_inplace(arr, rotations)
print(result)
# Output: [4, 5, 1, 2, 3]
