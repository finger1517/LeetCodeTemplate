import sys
from typing import get_origin
arr = []



try:
    while True:
        line = sys.stdin.readline()
        if line =='':
            break
        else:
            line = line.strip().split()
        # print(line)
        u = int(line[1])
        v = int(line[2])
        p = (1.0-(v-u)/10)*(v-u)
        arr.append((line[0],u,v,p))
except:
    pass


ans = []
max_sum = 0

# vis: wether List i is visited
# tmp_ans: the pattern that we make
# s: sum of the tickets
# idx: the id of the possible way
def dfs(vis,tmp_ans, s, idx):
    global max_sum, ans
    if idx==len(arr):
        # print(type(s))
        # print(type(max_sum))
        if s>max_sum:
            max_sum = s
            ans = tmp_ans
        return
    name,u,v,p = arr[idx]
    flag = True
    for i in range(u,v):
        if vis[i]:
            flag = False
            break
    if flag:
        for i in range(u,v):
            vis[i] = True
        dfs(vis,tmp_ans+[name], p+s, idx+1)
        for i in range(u,v):
            vis[i] = False
    dfs(vis, tmp_ans, s, idx+1)


vis = [False for _ in range(6)]
dfs(vis,[],0,0)
print(" ".join(ans))
    
