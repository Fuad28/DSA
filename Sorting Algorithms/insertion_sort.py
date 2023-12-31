def insertion_sort(arr: list) -> list:  # time: O(n^2) space: O(1)

    for i in range(1, len(arr)):
        j = i

        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr


print(insertion_sort([5, 9, 3, 1, 2, 8, 4, 7, 6]))
