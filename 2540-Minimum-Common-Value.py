from typing import List
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # 核心:双指针 哪个指针对应的元素小 哪个指针就右移
        pointer1=pointer2=0
        m,n=len(nums1),len(nums2)
        while pointer1<m and pointer2<n:
            if nums1[pointer1]==nums2[pointer2]:
                return nums1[pointer1]
            elif nums1[pointer1]<nums2[pointer2]:
                pointer1+=1
            else:
                pointer2+=1
        return -1
