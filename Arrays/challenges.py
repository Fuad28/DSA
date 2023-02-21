#missing number 

def find_missing(arr):
    for i in range(len(arr) -1 ):
        if arr[i + 1] - arr[i] > 1:
            arr.insert(i+1, arr[i] + 1)
            find_missing(arr)
    
    return arr

# print(find_missing([1, 3, 4, 7, 10]))

#Pairs/Two sum -LeetCode 1
def two_sum(arr, target):
    for idx1, i in enumerate(arr): #[1, 2, 3, 4, 5, 6]
        for j in arr[idx1+1:]:
            if i == j: continue
            if i + j == target: return([arr.index(i), arr.index(j)])
    return None
# print(two_sum([3, 2, 4], 6))


#rotate matrix
# import numpy as np
# np.random.seed(10)

# arr1= np.random.randint(low=1, high= 10, size= (4, 4))
# print(arr1)


"""2D Lists
Given 2D list calculate the sum of diagonal elements.

Example

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
sumDiagonal(myList2D) # 15
"""
def sum_diagonal(a):
    """
    [[1,2,3],
    [4,5,6],
    [7,8,9]]
    """
    assert len(a) == len(a[0]), "Only square matrix can have diagonals"

    diag_sum= 0
    for i in range(len(a)):
        diag_sum+= a[i][i]
    
    return diag_sum


# print(sum_diagonal([[1,2,3],[4,5,6],[7,8,9]]))


"""Best Score
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList) # 90 87
"""
def first_second(givenList):
    max_1, max_2= 0, 0

    for i in givenList:
        if (i > max_1):
            max_2= max_1
            max_1= i

    return max_1, max_2
        
# print(first_second([84,85,86,87,85,90,85,83,23,45,84,1,2,0]))


"""
Duplicate Number
Write a function to find the duplicate number on given integer array/list.

Example

removeDuplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
"""

def remove_duplicates(myList):
    uniques= []

    for i in myList: 
        if i not in uniques: uniques.append(i)
    
    return uniques
# print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))


"""
Pairs
Write a function to find all pairs of an integer array whose sum is equal to a given number.

Example

pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']
"""

def pair_sum(mylist, sum_):
    sum_list= []

    for idx, i in enumerate(mylist):
        for j in mylist[idx+1:]:
            if i + j == sum_: sum_list.append(f"{i}+{j}")
    
    return sum_list


print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))
