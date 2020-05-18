class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        x = sorted([c for c in s])
        y = sorted([c for c in t])
        char_pairs = zip(x, y)
        for a, b in char_pairs:
            print(a, b)
            if a != b:
                return False
        return True

s = "anagram"
t = "nagaram"
# s = "a"
# t = "ab"
sol = Solution()
print(sol.isAnagram(s, t))
