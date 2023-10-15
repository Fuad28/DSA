# Microsoft Array Question: Cnntainer with most water (medium)

from typing import Union
# brute force, T: O(n^2), S: O(1)
def max_area_1(array: list[int]) -> int:
    max_area= 0

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            area= min(array[i], array[j]) * (j - i)

            if area > max_area:
                max_area= area
                continue
    
    return max_area

# pointers T: O(n), S: O(1)
def max_area_2(array: list[int]) -> int:
    max_area= 0
    l, r= 0, len(array)

    while l < r:
        area= (array[l], array[r]) * (r - l)
        max_area= max(area, max_area)

        if array[l] > array[r]:
            r-= 1
        else:
            l+= 1 

    return max_area




# [5, 9, 2, 1, 4])) 16
