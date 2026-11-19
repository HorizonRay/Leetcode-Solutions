from typing import List
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
      # 回溯法
      def backtrace(path,used):
            if len(path)==len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i]=True
                    backtrace(path,used)
                    path.pop()
                    used[i]=False

        result=[]
        used=[False]*len(nums)
        backtrace([],used)
        return result
