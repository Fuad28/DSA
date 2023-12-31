
def merge_sort(input_arr):
    arr = []

    if len(input_arr) <= 1:
        return input_arr

    # find middle of array
    mid_idx = len(input_arr) // 2

    # Create left_arr ← arr[start..mid] and right_arr ← arr[mid+1..end]
    left_arr = input_arr[:mid_idx]
    right_arr = input_arr[mid_idx:]

    # sort the two halves
    merge_sort(left_arr)
    merge_sort(right_arr)

    # Initial values for pointers that we use to keep track of where we are in each array
    # i for left_arr, j for right_arr and k for final sorted arr.
    i = j = k = 0

    # Compare corresponding values of left and right arrays and add the smallest to the final sorted arr.
    # until at least one of the arrays is exhausted.
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1

        else:
            arr[k] = right_arr[j]
            j += 1

        k += 1

    # pick up the remaining elements in the array left and put in sorted array.
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    print(f"arr: {arr} ---- left_arr: {left_arr} --- right_arr: {right_arr}")

    return arr


print(merge_sort([5, 9, 3, 1, 2, 8, 4, 7, 6]))

"""

arr: [5, 9] ---- left_arr: [5] --- right_arr: [9]
arr: [1, 3] ---- left_arr: [3] --- right_arr: [1]
arr: [1, 3, 5, 9] ---- left_arr: [5, 9] --- right_arr: [1, 3]
arr: [2, 8] ---- left_arr: [2] --- right_arr: [8]
arr: [6, 7] ---- left_arr: [7] --- right_arr: [6]
arr: [4, 7, 6] ---- left_arr: [4] --- right_arr: [6, 7]
arr: [2, 4, 7, 6, 8] ---- left_arr: [2, 8] --- right_arr: [4, 7, 6]
arr: [1, 2, 3, 4, 5, 7, 6, 8, 9] ---- left_arr: [1, 3, 5, 9] --- right_arr: [2, 4, 7, 6, 8]

"""
