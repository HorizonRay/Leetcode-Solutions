class Solution:
    def pathEncryption(self, path: str) -> str:
        # 使用replace()函数 但不是原地修改
        path=path.replace('.',' ')
        return path
