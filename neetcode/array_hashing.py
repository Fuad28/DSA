from typing import List
from collections import defaultdict


# Contains Duplicate: https://leetcode.com/problems/contains-duplicate/ Easy

class Solution:  # time: O(n) space: O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False


# valid anagram: https://leetcode.com/problems/valid-anagram/ Easy

# solution 1
class Solution:  # time: O(nlogn) space: O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# two sum: https://leetcode.com/problems/two-sum/ Easy

# solution 1
class Solution:  # time: O(n^2) space: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and (nums[i] + nums[j] == target):
                    return [i, j]

# solution 2


class Solution:  # time: O(n) space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for idx, j in enumerate(nums):
            i = target - j

            if (i in nums_dict):
                return [idx, nums_dict[i]]

            nums_dict[j] = idx


# Group Anagrams: https://leetcode.com/problems/group-anagrams/ Medium

# solution 1
class Solution:  # time: O(mnlogn) space: O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_dict = defaultdict(list)

        for word in strs:
            output_dict["".join(sorted(word))].append(word)

        return output_dict.values()


# solution 2
class Solution:  # time: O(mn) space: O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(word)

        return res.values()


# Top K Frequent Elements: https://leetcode.com/problems/top-k-frequent-elements/ Medium

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = {}
        freq_map = {count: [] for count in range(1, len(nums) + 1)}
        output_arr = []

        for num in nums:
            mapper[num] = mapper.get(num, 0) + 1

        for num, count in mapper.items():
            freq_map[count].append(num)

        for i in range(len(nums), -1, -1):
            if len(output_arr) != k:
                output_arr.extend(freq_map[i])

        return output_arr


#  Product of Array Except Self: https://leetcode.com/problems/product-of-array-except-self/ Medium

# solution 1
class Solution: # time: O(n^2) space: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:                
        prod_arr= []

        for i in range(len(nums)):
            exempt_arr= nums[0: i] + nums[i+1:]
            prod= 1

            for j in exempt_arr:
                prod *= j
            
            prod_arr.append(prod)

        
        return prod_arr


# Solution 2
class Solution:  # time: O(n) space: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:                
        output_arr= [1] * len(nums)
        prefix, suffix= 1, 1

        for i in range(len(nums)):
            if i != 0:
                output_arr[i]= nums[i -1] * prefix
                prefix= output_arr[i]

        for i in range(len(nums) -1, -1, -1):
            if i != len(nums) - 1:
                output_arr[i]= output_arr[i] * nums[i + 1] * suffix
                suffix= nums[i + 1] * suffix

        
        return output_arr




# Valid sudoku: https://leetcode.com/problems/valid-sudoku/ Medium
class Solution: # time: O(1), space: O(1)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols= defaultdict(set)
        rows= defaultdict(set)
        squares= defaultdict(set) # key is (row/3, col/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[r] or 
                    board[r][c] in squares[(r//3,c//3)]
                ):

                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        return True

        

# Encode and Decode Strings: https://www.lintcode.com/problem/659/ Medium
class Solution: # time: O(n), space: O(n)
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoded_str= ""

        for word in strs:
            encoded_str += str(len(word)) + "#" + word
        
        return encoded_str

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    
    def decode(self, str):
        i= 0
        output_arr= []

        while i < len(str):
            j = i

            while str[j] != "#":
                j += 1
            
        
            word_length= int(str[i: j])
            i = j + 1
            j = i + word_length

            output_arr.append(str[i : j])


        return output_arr


# Valid strings: https://leetcode.com/problems/valid-parentheses/ Easy
class Solution: # time: O(n), space: O(n)
    def isValid(self, s: str) -> bool:
        parentheses= {")": "(", "}": "{", "]": "["}
        stack= []

        for i in s:
            if i not in parentheses:
                stack.append(i) # it's an open parenthesis
            
            else:
                if len(stack) == 0:
                    return False

                if stack[-1] == parentheses[i]:
                    stack.pop()
                
                else:
                    return False
            
        return len(stack) == 0


            
#Longest Consecutive Sequence: https://leetcode.com/problems/longest-consecutive-sequence/ medium
class Solution: # time: O(n), space: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums)
        longest= 0

        for i in nums:

            if (i - 1) not in nums: # start of a sequence
                seq_length= 0
                while (i + seq_length) in numSet:
                    seq_length += 1
            
                longest = max(longest, seq_length)
        
        return longest