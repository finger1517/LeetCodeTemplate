# 一个N*N的网格图内有M个特殊格子，你可以进行【两次】操作(M与N同阶)

# 选中【连续】K1个行，覆盖选中行内的所有特殊格子
# 选中【连续】K2个列，覆盖选中列内的所有特殊格子
# 你的目标是覆盖所有特殊格子，操作的总代价是(K1 + K2)，求最小代价(0 <= K1, K2 <= N)

# 例：

# N = 4, special = [(1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (4, 2), (4, 3)]

# 形成的图案为(1为特殊格子)：

# 0 1 1 0

# 1 1 1 1

# 0 1 1 0

# 0 1 1 0

# 答案为3，选中第2行以及第2-3列即可覆盖所有特殊格子

 

# 0 - i-1

# j +1 - N
N = 4
special = []


def judge(interval,specials):
    a,b = interval
    residual = [special for special[0] in specials and (special[0]<a or special[0]>b) ]
    if not residual:
        return 0
    residualcol = [resi[1] for resi in residual]

    residualcolmax = max(residualcol)

    residualcolmin = min(residualcol)

    return residualcolmax-residualcolmin+1

minnum = N
for i in range(len(N)-1):
    for j in range(i,len(N)-1):
        col_interval = judge([i,j],special)
        minnum = min(minnum,col_interval+(j-i+1))
print(minnum)
