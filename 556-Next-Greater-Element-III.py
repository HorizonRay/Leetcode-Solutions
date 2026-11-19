class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n=str(n)
        if len(n)==1:
            return -1
        nums=[x for x in n]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                for j in range(len(nums)-1,i,-1):
                    if nums[j]>nums[i]:
                        nums[i],nums[j]=nums[j],nums[i]
                        left,right=i+1,len(nums)-1
                        while left<right:
                            nums[left],nums[right]=nums[right],nums[left]
                            left+=1
                            right-=1
                        result=int(''.join(nums))
                        if result>=-2**31 and result<=2**31-1:
                            return result
        return -1
