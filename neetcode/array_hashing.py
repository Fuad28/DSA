from typing import List


# Contains Duplicate: https://leetcode.com/problems/contains-duplicate/

class Solution:  # time: O(n) space: O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False


# valid anagram: https://leetcode.com/problems/valid-anagram/

# solution 1
class Solution:  # time: O(nlogn) space: O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# two sum: https://leetcode.com/problems/two-sum/

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
