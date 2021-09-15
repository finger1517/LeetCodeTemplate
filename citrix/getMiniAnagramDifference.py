
def getMiniAnagram(str1,str2):
    if len(str1)!=len(str2):
        return -1
    if str1==str2:\
        return 0
    counter = {i:0 for i in 'abcdefghijklmnopqrstuvwxyz'}
    for i in range(len(str1)):
        counter[str1[i]]+=1
        counter[str2[i]]-=1
    res = 0
    for i in range(26):
        if counter[i]>0:
            res+=counter[i]
    return res
