class Solution:
    def cost(self , array ):
        # write code here
        n = len(array)
        arr = [0]*n
        for i in range(1,n):
            if array[i]>array[i-1]:
                arr[i] = arr[i-1] +1
            elif array[i]<array[i-1]:
                arr[i] = arr[i-1]-1
        k = min(arr)
        print("k:",k)
        return sum(arr)+n*(abs(k)+1)
        
# [编程题]最小金额购买商品
# 时间限制：C/C++ 1秒，其他语言2秒

# 空间限制：C/C++ 256M，其他语言512M

# 有一排商品，每一个商品都有自己的价值，现在需要花一定金额购买这些商品。规则是：如果一个商品的价值比它旁边的一个商品要高，那么这个商品就必须比它旁边的商品花费更多金额。所有的商品至少要进行一次金额购买。假设一次购买花费金额单位为1，最少需要多少金额可以购买所有商品？

# 现给定一个数组，数组元素表示每个商品的价值。请编写代码输出最少需要花费的金额。


# 输入例子1:
# [1,0,2]

# 输出例子1:
# 5