import random
from collections import defaultdict
class Solution:

    def __init__(self, nums: list[int]):
        self.idx=defaultdict(list) # 键值对的值是列表
        for i,num in enumerate(nums):
            self.idx[num].append(i)

    def pick(self, target: int) -> int:
        '''ans_list=self.idx[target] # 找到target键对应的键值对的值
        return ans_list[random.choice(len(ans_list))] # 在[0,len(ans_list)-1]双闭区间范围内随机取一个索引 然后在列表内找到对应值'''
        return random.choice(self.idx[target])
