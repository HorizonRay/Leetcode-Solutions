from typing import List
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]: # 从右向左找到相邻的左边元素nums[i]小于右边元素nums[i+1]的情况
                for j in range(n-1,i,-1): # 然后在区间(i,n-1]内从右向左找到第一个大于nums[i]的元素nums[j]
                    if nums[j]>nums[i]:
                        nums[i],nums[j]=nums[j],nums[i] # 然后交换位置
                        left,right=i+1,n-1 # 然后设定左指针为i+1 右指针为n-1
                        while left<right: # 在left<right的情况下交换元素并同时移动指针
                            nums[left],nums[right]=nums[right],nums[left]
                            left+=1
                            right-=1
                        return nums
        nums.sort() # 找不到就返回升序排列
