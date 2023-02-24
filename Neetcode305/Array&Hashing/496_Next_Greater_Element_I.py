# O(m*n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        
        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res
       
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
       
            
            res = [-1] * len(nums1)
            
            for i in range(len(nums1)):
                idx = self.findIdx(nums2, nums1[i])
                for j in range(idx,len(nums2)):
                    if nums2[j] > nums1[i]:
                        res[i] = nums2[j]
                        break
                    # not continue!
                    
            return res
        
    def findIdx(self,nums2,target):
                for i in range(len(nums2)):
                    if nums2[i] == target:
                        return i

        