class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not n:
            return
        if not m:
            nums2.reverse()
            for item in nums2:
                nums1.insert(0, item)
            del nums1[n:]
            return
        i = 0
        j = 0
        inserts = []
        #go through the initialized items
        while i < m:
            #if item should be inserted here
            if j < n and nums1[i] >= nums2[j]:
                while j < n and nums1[i] >= nums2[j]:
                    #make note to insert item and consider next item to be inserted
                    inserts.append([i, nums2[j]])
                    j += 1
            i += 1
        #remaining items just go on the end.
        i = 0
        inserts.reverse()
        print(inserts)
        for index, item in inserts:
            nums1.insert(index, item)
            i += 1
        for item in nums2[i:]:
            nums1.insert(m+i, item)
            i += 1
        del nums1[m+i:]

sol = Solution()
A = [0, 0, 0, 0, 0]
m = 0
B = [1, 2, 3, 4, 5]
n = 5
# A = [1,2,3,0,0,0]
# m = 3
# B = [2,5,6]
# n = 3
sol.merge(A,m,B,n)
print(A)
