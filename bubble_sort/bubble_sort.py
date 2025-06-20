def bubble_sort(unsorted_list, size):
    for n in range(size - 1):  # Loop size - 1 times
        swapped = False
        for i in range(size - 1 - n):  # Compare up to the last sorted element
            if unsorted_list[i] > unsorted_list[i + 1]:
                # Swap elements
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
                swapped = True

        # If no elements were swapped, the list is already sorted
        if not swapped:
            break

# Test the function
unsorted_list = [5, 4, 3, 2, 1, 0]
size = len(unsorted_list)

bubble_sort(unsorted_list, size)

print("Sorted list is:")
print(unsorted_list)
