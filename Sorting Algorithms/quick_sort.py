def swap(arr, idx_1, idx_2):
    arr[idx_1], arr[idx_2] = arr[idx_2], arr[idx_1]


def pivot(arr):
    swap_idx = pivot_idx = 0

    for i in range(1, len(arr)):
        if arr[i] < arr[pivot_idx]:
            swap_idx += 1
            swap(arr, swap_idx, i)

    swap(arr, swap_idx, pivot_idx)

    return swap_idx  # which is the new idx of the pivot element


def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_idx = pivot(arr)
    print(
        f"left: {arr[:pivot_idx]}  --- pivot: {[arr[pivot_idx]]} --- right: {arr[pivot_idx+1:]}")
    left_arr = quick_sort(arr[:pivot_idx])
    right_arr = quick_sort(arr[pivot_idx+1:])

    print(f"arr_out: {left_arr + [arr[pivot_idx]] + right_arr} \n\n")

    return left_arr + [arr[pivot_idx]] + right_arr


print(quick_sort([5, 9, 3, 1, 2, 8, 4, 7, 6]))


"""

left: [4, 3, 1, 2]  --- pivot: [5] --- right: [8, 9, 7, 6]
left: [2, 3, 1]  --- pivot: [4] --- right: []
left: [1]  --- pivot: [2] --- right: [3]
arr_out: [1, 2, 3] 


arr_out: [1, 2, 3, 4] 


left: [6, 7]  --- pivot: [8] --- right: [9]
left: []  --- pivot: [6] --- right: [7]
arr_out: [6, 7] 


arr_out: [6, 7, 8, 9] 


arr_out: [1, 2, 3, 4, 5, 6, 7, 8, 9] 
"""
