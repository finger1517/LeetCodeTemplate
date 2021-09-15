#
# retrun the longest increasing subsequence
# @param arr int整型一维数组 the array
# @return int整型一维数组
#

def LIS(arr ):
    # write code here
    n = len(arr)
    dp = [1]*n
    dp1 = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i] = max(dp[i],dp[j]+1)
    ans = 0
    max_ind = 0
    for i in range(n):
        if dp[i]>ans:
            ans = dp[i]
            max_ind = i
    
    print(dp)

    res = []
    ind = max_ind

    print("ans:",ans)
    print("ind:",ind)
    # j = 1
    cur = arr[ind]
    res.append(arr[ind])
    # while j<ans:
    #     ind-=1
    #     if arr[ind]<cur:
    #         print(ind)
    #         cur = arr[ind]
    #         res.append(cur)
    #         j+=1
    #     else:
    #         pass
    # return res[::-1]
    for j in range(ind-1,-1,-1):
        if arr[j]<cur and dp[j]==ans-1:
            ans-=1
            cur = arr[j]
            res.append(cur)
    return res[::-1]
        
print(LIS([2,1,5,3,6,4,8,9,7]))

# [2,1,5,3,6,4,8,9,7]
# [1,3,4,8,9]



