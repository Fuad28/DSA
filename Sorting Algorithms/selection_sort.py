def selection_sort(arr: list) -> list:  # time: O(n^2) space: O(1)

    for i in range(len(arr)):
        min_idx = i

        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


print(selection_sort([5, 9, 3, 1, 2, 8, 4, 7, 6]))
