from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrace(path,used):
            if len(path)==len(nums):
                result.append(path[:])
                return
            visited=set()
            for i in range(len(nums)):
                if used[i]:
                    continue
                if nums[i] in visited:
                    continue
                visited.add(nums[i])
                used[i]=True
                path.append(nums[i])
                backtrace(path,used)
                used[i]=False
                path.pop()

        result=[]
        used=[False]*len(nums)
        backtrace([],used)
        return result
