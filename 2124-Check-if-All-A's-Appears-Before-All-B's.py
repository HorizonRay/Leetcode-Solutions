class Solution:
    def checkString(self, s: str) -> bool:
        b=False
        for c in s:
            if c=='b':
                b=True
            elif c=='a' and b: # 说明已经遇到b了 但是之后又遇到a
                return False
        return True
