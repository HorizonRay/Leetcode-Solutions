class ProductOfNumbers:
    # 核心:后缀乘积
    def __init__(self):
        self.prefix_product=[1]

    def add(self, num: int) -> None:
        if num!=0:
            self.prefix_product.append(self.prefix_product[-1]*num)
        else: # 当num为0的时候 说明从这里到前面的后缀乘积为0 直接舍弃前面的元素 防止空间过大(题目元素只会不停增加)
            self.prefix_product=[1]

    def getProduct(self, k: int) -> int:
        n=len(self.prefix_product)
        if n>=k+1: # 符合范围条件
            return self.prefix_product[-1]//self.prefix_product[n-k-1]
        else: # 超过查询范围 实际上乘积是0
            return 0
