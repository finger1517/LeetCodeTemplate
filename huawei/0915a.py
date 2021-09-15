works = input().strip().split()
works = sorted([int(x)for x in works])
tools = input().strip().split()
tools = sorted([int(x)for x in tools])

ans = 1
idx = 0
for w in works:
    while idx<len(tools) and tools[idx]<w:
        idx+=1
    tmp = 1e9+10
    if idx-1>=0:
        tmp = min(tmp, abs(w-tools[idx-1]))
    
    if idx!=len(tools):
        tmp = min(tmp, abs(w-tools[idx]))
    
    ans = max(ans,tmp)
print(ans)


