# 顺时针回形打印数组
# 详细描述
# 对于给定的数组，按回形从外向内顺时针顺序遍历整个数组，如:

# [[1,2,3,4],  [12,13,14,5],  [11,16,15,6],  [10,9,8,7]]
# 输出为：1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16

# 其他
# 时间限制: 1000ms

# 内存限制: 256.0MB

# 输入输出示例
# 示例1
# 输入
# 复制
# [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
# 输出
# 复制
# "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16"

def printClockwise( inputMat) :
    # write code here
    mat = inputMat
    if not mat: return []
    l, r, t, b, res = 0, len(mat[0]) - 1, 0, len(mat) - 1, []
    while True:
        for i in range(l, r + 1): res.append(mat[t][i]) # left to right
        t += 1
        if t > b: break
        for i in range(t, b + 1): res.append(mat[i][r]) # top to bottom
        r -= 1
        if l > r: break
        for i in range(r, l - 1, -1): res.append(mat[b][i]) # right to left
        b -= 1
        if t > b: break
        for i in range(b, t - 1, -1): res.append(mat[i][l]) # bottom to top
        l += 1
        if l > r: break
    res = list(map(str,res))
    return ",".join(res)

mat = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
print(printClockwise(mat))