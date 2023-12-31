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

class Solution:  # time: O(n) space: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = defaultdict(self.zero)
        freq_map = {count: [] for count in range(1, len(nums) + 1)}
        output_arr = []

        for num in nums:
            mapper[num] += 1

        for num in mapper:
            freq_map[mapper[num]].append(num)

        for i in range(len(nums), -1, -1):
            if len(output_arr) != k:
                output_arr.extend(freq_map[i])

        return output_arr

    def zero(self):
        return 0
