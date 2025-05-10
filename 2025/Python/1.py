def isprime(x):# 素数筛
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def check(y):
    a = y % 10
    b = y // 10 % 10
    c = y // 100 % 10
    return (a + b) % 10 == c

m,n = map(int, input().split())
cnt = 0 # 计数器 实现每五个输出一个换行
for i in range(n, m-1,-1): # 反向遍历实现输出从小到大
    if isprime(i) and check(i):
        cnt += 1
        if cnt % 5 == 0:
            print(i)
        else:
            print(i, end=' ')
