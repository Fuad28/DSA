
def merge_sort(arr: list):
    came_in = arr.copy()

    if len(arr) <= 1:
        return arr

    # find middle of array
    mid_idx = len(arr) // 2

    # Create left_arr ← arr[start..mid] and right_arr ← arr[mid+1..end]
    left_arr = arr[:mid_idx]
    right_arr = arr[mid_idx:]

    # sort the two halves
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    # Initial values for pointers that we use to keep track of where we are in each array
    # i for left_arr, j for right_arr and k for final sorted arr.
    i = j = k = 0

    # Compare corresponding values of left and right arrays and add the smallest to the final sorted arr.
    # until at least one of the arrays is exhausted.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # pick up the remaining elements in the array left and put in sorted array.
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    print(
        f"arr_came_in: {came_in} -- arr: {arr} ---- left: {left} --- right: {right}")

    return arr


print(merge_sort([5, 9, 3, 1, 2, 8, 4, 7, 6]))

"""

arr: [5, 9] ---- left: [5] --- right: [9]
arr: [1, 3] ---- left: [3] --- right: [1]
arr: [1, 3, 5, 9] ---- left: [5, 9] --- right: [1, 3]
arr: [2, 8] ---- left: [2] --- right: [8]
arr: [6, 7] ---- left: [7] --- right: [6]
arr: [4, 7, 6] ---- left: [4] --- right: [6, 7]
arr: [2, 4, 7, 6, 8] ---- left: [2, 8] --- right: [4, 7, 6]
arr: [1, 2, 3, 4, 5, 7, 6, 8, 9] ---- left: [1, 3, 5, 9] --- right: [2, 4, 7, 6, 8]




[1, 2, 3, 4, 5, 7, 6, 8, 9]

"""
