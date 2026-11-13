from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # 字典模拟哈希表映射
        result=['']
        map={'2':'abc','3':'def','4':'ghi',
         '5':'jkl','6':'mno','7':'pqrs',
         '8':'tuv','9':'wxyz'}
        for i in digits: # 逐位处理
            transition=[]
            for j in result: # 已有的部分组合
                for k in map[i]: # 当前位可选的字母
                    transition.append(j+k)
            result=transition
        return result
