from typing import List
import copy
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def appendi(transition,element):
            for x in transition:
                x.append(element)
            return transition

        result=[]
        nums.sort()
        transition=[[],[nums[0]]]
        n=len(nums)
        if n==1:
            return transition
        for i in range(1,n): # 使用深拷贝进行答案的更新
            result=copy.deepcopy(transition)
            a=appendi(transition,nums[i])
            tran=[tuple(x) for x in result]
            for x in a:
                map=set(tran)
                if tuple(x) in map:
                    continue
                result.append(x)
            transition=copy.deepcopy(result)
        return result
