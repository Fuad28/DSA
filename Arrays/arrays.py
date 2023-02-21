#creating an array
from array import *

# arr1= array('i', [1, 2, 3, 4, 5])
# arr1.insert(4, 7)
# # print(arr1)

# def traverse_arr(arr):
#     for i in arr:
#         print(i)

# # traverse_arr(arr1)


# def search_arr(arr, value):
#     for val in arr:
#         if val == value:
#             return arr.index(value)
#     return f"{value} not in array"

# print(search_arr(arr1, 8))

#2-d arrays 
import numpy as np
arr1= np.array([[11, 15, 10, 6], [10, 14, 11, 15], [12, 17, 12, 8], [15, 18, 14, 9]])

arr2= np.insert(arr1, 1, [[0, 0, 0, 0]], axis= 0) #insert [0,0,0,0] to row 1 of arr1
# print(arr2)
arr3= np.append(arr2, [[0, 0, 0, 0]], axis= 0)
# print(arr3)

def accessItem(arr, row_index, col_index):
    if (row_index >= arr.shape[0]) or (col_index >= arr.shape[1]):
        print("Invalid index")
    else:
        return arr[row_index][col_index]
# print(accessItem(arr3, 6, 4))

#traversal
# print(arr3)
# def traverse_arr(arr):
#     for row in range(arr.shape[0]):
#         for col in range(arr.shape[1]):
#             print(arr[row][col])

# traverse_arr(arr3)

#search
# def search_arr(arr, value):
#     for row in range(arr.shape[0]):
#         for col in range(arr.shape[1]):
#             if arr[row][col] == value: return (row, col)
#     return f"{value} not in array"
        

# print(search_arr(arr3, 9))

#delete element
print(arr3)
arr4= arr3.copy()
arr4= np.delete(arr4, 1, axis= 0) #delete axis 0 (row) 1 of arr 4
print(arr4)