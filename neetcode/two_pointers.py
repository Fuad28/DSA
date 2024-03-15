
from types import List
# Valid palindrome: https://leetcode.com/problems/valid-palindrome/description/ Easy

# solution 1
class Solution: # time: O(n), space: O(n)
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char.lower() for char in s if char.isalnum()])

        return s == s[::-1]
        

# solution 2: same as 1
class Solution: # time: O(n), space: O(n)
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char.lower() for char in s if char.isalnum()])
        reversed_s = ""
        count= -1

        while count >= -len(s):
            
            reversed_s += s[count]
            count -= 1
        
        return s == reversed_s
        

# solution 3:
class Solution: # time: O(n), space: O(1)
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right= len(s) - 1

        while left < right:
            while (left < right) and (not self.isalnum(s[left])):
                left += 1
            
            while (left < right) and (not self.isalnum(s[right])):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1


        return True
    

    def isalnum(self, char):

        return (
            ord("A") <= ord(char) <= ord("Z") or
            ord("a") <= ord(char) <= ord("z") or
            ord("0") <= ord(char) <= ord("9")
        ) 


# Two Sum II - Input Array Is Sorted: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# solution 1
class Solution: # time: O(n^2), space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i= 0

        while i <= len(numbers):
            j = i + 1

            while j < len(numbers):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                
                j += 1
            
            i += 1
                

# solution 2
class Solution: # time: O(n), space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right= 0, len(numbers) -1

        while True:
            _sum = numbers[left] + numbers[right]

            if _sum > target:
                left += 1

            elif _sum > target:
                right -= 1

            else:
                return [left+1, right+1]


# Container With Most Water: https://leetcode.com/problems/container-with-most-water/
# solution 1
class Solution:# time: O(n), space: O(1)
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        max_area = 0

        while left < right:
            h= min(height[left], height[right])
            w= right - left
            area= h * w
            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1
            
            else:
                right -= 1
        
        return max_area


# Palindromic Substrings: https://leetcode.com/problems/palindromic-substrings/description/
class Solution: # time: O(n^2), space: O(1)
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            l = r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        return count


# Trapping Rain Water: https://leetcode.com/problems/trapping-rain-water/description/

# solution 1
class Solution: # time: O(n), space: O(n)
    def trap(self, height: List[int]) -> int:
        total_water_trapped = 0

        for i in range(len(height)):
            left_max = right_max = 0
            left_arr = height[:i]
            right_arr= height[i: ]

            if len(left_arr):
                left_max = max(left_arr)
            
            if len(right_arr):
                right_max = max(right_arr)

            water_trapped = min(left_max, right_max) - height[i]

            if water_trapped > 0:
                total_water_trapped += water_trapped
        
        return total_water_trapped


# solution 2
class Solution: # time: O(n^2), space: O(1)
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1 
        left_max, right_max = height[l], height[r]
        total_water_trapped = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                total_water_trapped += left_max - height[l]
            
            else:
                r -= 1
                right_max = max(right_max, height[r])
                total_water_trapped += right_max - height[r]
        
        return total_water_trapped

        