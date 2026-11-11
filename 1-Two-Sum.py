from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx={} # 用字典模拟哈希表 存储当前元素的当前最新索引
        for i,num in enumerate(nums):
            if target-num in idx: # target-num是两个加数中除了num的另外一个 检查是否存在于字典中 如果存在说明找到答案
                return [idx[target-num],i]
            idx[num]=i # 记录当前元素的索引
