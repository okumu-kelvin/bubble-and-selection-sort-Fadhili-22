def selection_sort(arr, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap
        arr[ind], arr[min_index] = arr[min_index], arr[ind]

# Test data and call — outside the function
arr = [5, 4, 3, 2, 1, 0]
size = len(arr)
selection_sort(arr, size)

print("Sorted array:")
print(arr)
