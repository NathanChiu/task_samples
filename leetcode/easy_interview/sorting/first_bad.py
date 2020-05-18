# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(n):
    if n >= 2:
        return True
    return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        if isBadVersion(n) and not isBadVersion(n-1):
            return n
        left = 1
        right = n
        mid = int(n/2)
        # i = 0
        while True:
            # print(left, mid, right)
            if isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                return mid
            if isBadVersion(mid):
                #go left
                right = mid
            else:
                #go right
                left = mid
            mid = int((right+left)/2)
            # i += 1


sol = Solution()
n = 4
print(sol.firstBadVersion(n))
