from typing import List
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # 数学规律:因为可以改动两个值 所以可以将其中两个值改成一样 最小差值就一定是0 然后尽量让最大差值变小
        # 改动值最好落在“剩余未修改元素”的极值范围内，比如直接改成剩余元素的最小值。
        nums.sort()
        # 第一种情况:将最小的两个值改掉
        # 第二种情况:将最大值和最小值改掉
        # 第三种情况:将最大的两个值改掉
        return min(nums[-1]-nums[2],nums[-2]-nums[1],nums[-3]-nums[0])
