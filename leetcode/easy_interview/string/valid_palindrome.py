import string
class Solution:
    def isPalindrome(self, s):
        x = reversed([c for c in s.lower() if c in string.digits or c in string.ascii_lowercase])
        y = [c for c in s.lower() if c in string.digits or c in string.ascii_lowercase]
        char_pairs = zip(x, y)
        for a, b in char_pairs:
            if a != b:
                return False
        return True

# s = "anagram"
# t = "nagaram"
# s = "a"
# t = "ab"
sol = Solution()
# s = "A man, a plan, a canal: Panama"
s = "race a car"
print(sol.isPalindrome(s))
