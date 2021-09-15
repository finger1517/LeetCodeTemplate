# "66"
# "6699"


def Paired69(S ):
    # write code here
    s = list(S)
    stack = []
    for i in s:
        if i=='6':
            stack.append(i)
        if i=='9':
            if stack and stack[-1]=='6':
                stack.pop()
            else:
                stack.append(i)

    if stack:
        amount9 = stack.count('9')
        amount6 = stack.count('6')
        return '6'*amount9+S+'9'*amount6
    else:
        return S

print(Paired69("9966"))
print(Paired69("66"))

# 成对的69
# 时间限制：C/C++ 1秒，其他语言2秒

# 空间限制：C/C++ 256M，其他语言512M

# 成对的69匹配序列定义为：

# 1、 空串""是一个成对的69序列；

# 2、如果"X"和"Y"是成对的69序列，那么"XY"也是成对的69序列；

# 3、如果"X"是一个成对的69序列，那么"6X9"也是一个成对的69序列；

# 4、每个成对的69序列都可以由以上规则生成。 例如，"", "69", "6699", "6969"都是成对的。

# 现在给出一个序列S，允许你的操作是： 在S的开始和结尾出添加一定数量的6或者9，使序列S变为一个成对的69序列。输出添加最少的6或者9之后成对的69序列是什么。


# 输入例子1:
# "66"

# 输出例子1:
# "6699"