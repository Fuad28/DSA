
def merge_sort(arr: list):  # time: O(nlogn) space: O(n)

    if len(arr) <= 1:
        return arr

    # find middle of array
    mid_idx = len(arr) // 2

    # Create left_arr ← arr[start..mid] and right_arr ← arr[mid+1..end]
    left_arr = arr[:mid_idx]
    right_arr = arr[mid_idx:]

    print(f"arr_in: {arr} -- left_in: {left_arr} -- right_in: {right_arr}")

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

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    print(f"left_out: {left} -- right_out: {right} -- arr_out: {arr}\n\n")

    return arr


print(merge_sort([5, 9, 3, 1, 2, 8, 4, 7, 6]))

"""
To better undertsand how the sorting was carried out.


arr_in: [5, 9, 3, 1, 2, 8, 4, 7, 6] -- left_in: [5, 9, 3, 1] -- right_in: [2, 8, 4, 7, 6]
arr_in: [5, 9, 3, 1] -- left_in: [5, 9] -- right_in: [3, 1]
arr_in: [5, 9] -- left_in: [5] -- right_in: [9]
left_out: [5] -- right_out: [9] -- arr_out: [5, 9]


arr_in: [3, 1] -- left_in: [3] -- right_in: [1]
left_out: [3] -- right_out: [1] -- arr_out: [1, 3]


left_out: [5, 9] -- right_out: [1, 3] -- arr_out: [1, 3, 5, 9]


arr_in: [2, 8, 4, 7, 6] -- left_in: [2, 8] -- right_in: [4, 7, 6]
arr_in: [2, 8] -- left_in: [2] -- right_in: [8]
left_out: [2] -- right_out: [8] -- arr_out: [2, 8]


arr_in: [4, 7, 6] -- left_in: [4] -- right_in: [7, 6]
arr_in: [7, 6] -- left_in: [7] -- right_in: [6]
left_out: [7] -- right_out: [6] -- arr_out: [6, 7]


left_out: [4] -- right_out: [6, 7] -- arr_out: [4, 6, 7]


left_out: [2, 8] -- right_out: [4, 6, 7] -- arr_out: [2, 4, 6, 7, 8]


left_out: [1, 3, 5, 9] -- right_out: [2, 4, 6, 7, 8] -- arr_out: [1, 2, 3, 4, 5, 6, 7, 8, 9]


[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
