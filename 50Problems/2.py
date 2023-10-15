# Google Array Question: valid mountain array (easy)


# T: O(n^2), S: O(1)
def valid_mountain(array: list[int]) -> bool:
    """
    Given an array of integers, return true if the following conditions are fufiled:
    a. length of the array is bigger than or equal to 3
    b. there exists some index i such that:
        a[0] < a[1]< .. < a[i] # strictly incresaing
        a[i] > a[i+1]< .. < a[len(array) - 1] # strictly decreasing
    """

    if not len(array) >= 3:
        return False
    
    i = 1

    while (i < len(array)) and (array[i - 1] < array[i]): # the climbing portion, breaks at the peak
        i += 1
    
    if i == 1: # it never climbed
        return False

    while (i < len(array)) and (array[i - 1] > array[i]): # the downing portion, stops at the end
        i += 1
    
    return i == len(array) # if it got to the end, it's a valid mountain array


            
print(valid_mountain([0, 3, 2, 1])) # True
print(valid_mountain([0, 3, 5, 5])) # False


