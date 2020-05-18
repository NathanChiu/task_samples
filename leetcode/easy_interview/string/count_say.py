class Solution:
    def findConsecutives(self, s):
        i = 0
        count = 0
        target = ""
        groups = []
        while i < len(s):
            if s[i] == target:
                count += 1
            else:
                groups.append(str(count)+target)
                target = s[i]
                count = 1
            i += 1
        groups.append(str(count)+target)
        return groups

    def getNthTerm(self, n):
        if n == 1:
            return "1"
        else:
            prev = self.getNthTerm(n-1)
            groups = self.findConsecutives(prev)
            del groups[0]
            s = "".join(groups)
            return s
    def countAndSay(self, n):
        return self.getNthTerm(n)
n = 1
sol = Solution()
print(sol.getNthTerm(4))
# print(sol.countAndSay(n))
# print(sol.findConsecutives("112233311"))
