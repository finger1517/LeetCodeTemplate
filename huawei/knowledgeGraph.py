# input
# 3
# student subClassOf person 
# Tom instanceOf student 
# Marry instanceOf person 
# person


hash = {}
instance = set()

n = int(input())
for i in range(n):
    line = input()
    a,b,c = line.split()
    if b=="instanceOf":
        instance.add(a)
    hash[a] = c

# print(hash)

ss = input()


ret = set()
for s in instance:
    s1 = s
    while hash.get(s):
        if hash[s1]==ss:
            ret.add(s)
            break
        s1 = hash[s1]

# print(ret)
ret = list(ret)
ret.sort()
ans = ""
if not ret:
    ans = "empty"

else:
    i=0
    for s in ret:
        if i==0:
            ans+=s
            i+=1
            # print(ans)
        else:
            # print("\0",end='')
            ans+= " "+s
            i+=1

print(ans)
