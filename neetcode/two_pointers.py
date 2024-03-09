
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

        