

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

