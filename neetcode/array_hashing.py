# from typing import List


# # Contains Duplicate: https://leetcode.com/problems/contains-duplicate/

# class Solution:  # time: O(n) space: O(n)
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = set()

#         for num in nums:
#             if num in seen:
#                 return True

#             seen.add(num)

#         return False


# # valid anagram: https://leetcode.com/problems/valid-anagram/

# # solution 1
# class Solution:  # time: O(nlogn) space: O(1)
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)


# # two sum: https://leetcode.com/problems/two-sum/

# # solution 1
# class Solution:  # time: O(n^2) space: O(1)
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if (i != j) and (nums[i] + nums[j] == target):
#                     return [i, j]

nums = [3, 3]
target = 6

nums_dict = {i: j for i, j in enumerate(nums)}
print(nums_dict)
for j in nums_dict:
    i = target - j
    print(nums_dict[j], nums_dict[i])
    if (i in nums_dict) and (nums_dict[j] != nums_dict[i]):
        print(nums_dict[j], nums_dict[i])
