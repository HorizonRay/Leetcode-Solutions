from typing import List
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict
        groups=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1 # 统计每个字符串的字母个数 并将count整体作为键
            groups[tuple(count)].append(s) # 键必须是不可变的数据类型
        return list(groups.values())
