from math import sqrt, ceil, floor


def insertion_sort(arr: list) -> list:  # time: O(n^2) space: O(1)

    for i in range(1, len(arr)):
        j = i

        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr


def bucket_sort(arr: list) -> list:  # time: O(n^2) space: O(1)
    no_of_buckets = round(sqrt(len(arr)))
    buckets = [[] for _ in range(no_of_buckets)]
    max_value = max(arr)

    for i in arr:
        bucket_idx = ceil((i*no_of_buckets)/max_value) - 1
        buckets[bucket_idx].append(i)

    arr.clear()

    for idx in range(no_of_buckets):
        arr.extend(insertion_sort(buckets[idx]))  # quicksort is better here.

    return arr


print(bucket_sort([5, 9, 3, 1, 2, 8, 4, 7, 6]))


def bucket_sort_neg(arr):
    number_of_buckets = round(sqrt(len(arr)))
    min_value = min(arr)
    max_value = max(arr)
    range_val = (max_value - min_value) / number_of_buckets

    buckets = [[] for _ in range(number_of_buckets)]

    for j in arr:
        if j == max_value:
            buckets[-1].append(j)
        else:
            index_b = floor((j - min_value) / range_val)
            buckets[index_b].append(j)

    sorted_array = []
    for i in range(number_of_buckets):
        buckets[i] = insertion_sort(buckets[i])
        sorted_array.extend(buckets[i])

    return sorted_array
