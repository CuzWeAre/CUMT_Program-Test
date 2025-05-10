def iswave(x):
    s = str(x)
    if len(s) < 3:
        return False
    l,r = s[0],s[1]
    for i in range(len(s)):
        c = l if i % 2 == 0 else r
        if c != s[i]:
            return False
    return True
        
def change(num,r):
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    while num > 0:
        res = s[num % r] + res
        num //= r
    if res:
        return res
    return '0'

r1,r2,n1,n2,k = map(int, input().split())
for i in range(n1,n2+1):
    cnt = 0
    for j in range(r1,r2+1):
        if iswave(change(i,j)):
            cnt += 1
    if cnt >= k:
        print(i, end=' ')

