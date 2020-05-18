class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) < len(nums2):
            sorted_1 = sorted(nums1)
            sorted_2 = sorted(nums2)
        else:
            sorted_1 = sorted(nums2)
            sorted_2 = sorted(nums1)
        #sorted 1 is the smaller list
        i = 0
        j = 0
        result = []
        while i < len(sorted_1) and j < len(sorted_2):
            # print('inds:', i, j)
            # print('lengths', len(sorted_1), len(sorted_2))
            if sorted_1[i] == sorted_2[j]:
                #remove from both and add to result
                result.append(sorted_1[i])
                del sorted_1[i]
                del sorted_2[j]
            elif sorted_1[i] > sorted_2[j]:
                #move along the j-indexed list
                j += 1
            elif sorted_1[i] < sorted_2[j]:
                i += 1
        return result

sol = Solution()
# A = [1,2,2,1]
# B = [2, 2]
A = [4,7,9,7,6,7]
B = [5,0,0,6,1,6,2,2,4]
print(sol.intersect(A, B))
