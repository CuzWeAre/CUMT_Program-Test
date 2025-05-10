# 用了贪心，可能有问题，望补充指正

fibs = [1,1]
while fibs[-1] < 1000000000:# 先对数列打表
    fibs.append(fibs[-1] + fibs[-2])

t = int(input())
nums = [int(input()) for _ in range(t)]
ans = []
for num in nums:
    res = []
    remain = num
    for fib in fibs[::-1]:
        if fib <= remain:
            res.append(fib)
            remain -= fib
            if remain == 0:
                break
    ans.append(res)

for i in range(len(ans)):
    print(nums[i], end='=')
    print('+'.join(map(str, ans[i])))
