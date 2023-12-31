def bubble_sort_1(arr: list) -> list:

    while True:
        no_sorted = 0

        for i in range(0, len(arr)-1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                no_sorted += 1

        if no_sorted == 0:
            break

    return arr


print(bubble_sort_1([5, 9, 3, 1, 2, 8, 4, 7, 6]))


def bubble_sort_2(arr: list) -> list:  # time: O(n^2) space: O(1)

    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(bubble_sort_2([5, 9, 3, 1, 2, 8, 4, 7, 6]))
