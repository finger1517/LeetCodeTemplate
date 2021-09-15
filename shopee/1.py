
def char_and_num_return(text_source ):
    # write code here
    lis = text_source.split()
    string = []
    num = []
    for i in lis:
        try:
            a = int(i)
            num.append(a)
        except:
            string.append(i)
    num.sort()
    num = list(map(str,num))
    res = string+num
    return " ".join(res)


print(char_and_num_return("xb 1 cc 5 dd 10 ee 2"))

# 对于给定的一个
# 时间限制：C/C++ 1秒，其他语言2秒

# 空间限制：C/C++ 256M，其他语言512M

# 对于给定的一个包含连续字母、连续数字及空格的字符串（不会出现字母和数字连在一起出现），实现字母部分按出现顺序排列而数字按照从小到达顺序排在最后一个字母的后面

# 输入例子1:
# "xb 1 cc 5 dd 10 ee 2"

# 输出例子1:
# "xb cc dd ee 1 2 5 10"