tmp = input().strip().split()
avg = int(tmp[0])
n = int(tmp[1])

arr = input().strip().split()

arr = sorted([int(x) for x in arr],reverse=True)



mod_list = [[] for _ in range(avg)]
for num in arr:
    mod = num%avg
    mod_list[mod].append(num)

ans = []
flag = True
for mod, nums in enumerate(mod_list):
    if mod==0 or mod==avg-mod:
        if len(nums)%2==1:
            flag=False
            break
        else:
            for i in range(len(nums)//2):
                if nums[2*i]>nums[2*i+1]:
                    ans.append((nums[2*i],nums[2*i+1]))
                else:
                    ans.append((nums[2*i+1],nums[2*i]))
    else:
        if not len(nums)==len(mod_list[avg-mod]):
            flag=False
            break
        else:
            for num1,num2 in zip(nums, mod_list[avg - mod]):
                if num1<num2:
                    ans.append((num2,num1))
                else:
                    ans.append((num1,num2))
if not flag:
    print(0)
else:
    ans = sorted(ans, key=lambda x:(x[0]+x[1],x[0]), reverse=True)
    out = []
    for num1, num2 in ans:
        out.append(str(num1))
        out.append(str(num2))
    print(" ".join(out))