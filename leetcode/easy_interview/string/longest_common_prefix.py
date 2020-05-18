class Solution:

    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        min_len = min(map(len, strs))
        min_word = strs[list(map(len, strs)).index(min_len)]
        pref = ""
        if min_len > 0:
            i = 0
            while i < min_len:
                c = min_word[i]
                for s in strs:
                    if s[i] != c:
                        return pref
                pref = pref + c
                i += 1
        return pref


sol = Solution()
strs = ["flower","flow","flight"]
print(sol.longestCommonPrefix(strs))
# print(max(map(len,strs)))
# for i in map(len,strs):
#     print (i)
