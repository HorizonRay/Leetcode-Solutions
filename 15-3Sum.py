from typing import List
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 思路:升序排序后 固定左边一个指针 然后右边两个指针向中间收缩寻找答案
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(n-2): # 至少给右边预留两个元素 防止出界
            if nums[i]>0: # 左边指针对应的元素是目前最小的 而最小的元素都大于0 所以三数之和肯定大于0 且升序排序后的数组元素越往右边越大 所以没有答案了
                break
            elif i>0 and nums[i]==nums[i-1]: # 防止重复
                continue
            j,k=i+1,n-1 # 左右指针
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total==0:
                    ans.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]: # 检查左指针对应元素的右边相邻元素是否重复 是就跳过
                        j+=1
                    while j<k and nums[k]==nums[k-1]: # 检查右指针对应元素的左边相邻元素是否重复 是就跳过
                        k-=1
                    # total为0且跳过了重复元素 所以移动一边的指针肯定不符合答案 所以两个指针一起移动
                    j+=1
                    k-=1
                elif total>0: # 和过大 右指针左移
                    k-=1
                else: # 和过小 左指针右移
                    j+=1
        return ans
