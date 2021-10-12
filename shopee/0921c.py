# 最小加数个数
# 详细描述
# 输入一个数字，从给定数字项(20、10、5、4、2、1)中挑选n次(同一个数字可多次挑选)，要求这n个数字和等于输入数字，求输出n的最小值。例如输入8，输出2

# 其他
# 时间限制: 1000ms

# 内存限制: 256.0MB

# 输入输出描述
# 输入描述
# 输入数字

# 8

# 输出描述
# 输出n的最小值

# 2

# 输入输出示例
# 示例1
# 输入
# 复制
# 8
# 输出
# 复制
# 2

def minPlus(coins, amount):
    # 初始化
    dp = [amount + 1]*(amount + 1)
    dp[0] = 0
    # 遍历物品
    for coin in coins:
        # 遍历背包
        for j in range(coin, amount + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)
    return dp[amount] if dp[amount] < amount + 1 else -1

coins = [20,10,5,4,2,1]
amount = int(input())
print(minPlus(coins,amount))