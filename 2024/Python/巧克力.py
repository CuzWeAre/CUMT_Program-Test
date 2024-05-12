def cho_minx(cho0, n, k):
    x_min = 0
    for i in range(n):
        if min(cho0[i]) > x_min:
            x_min = min(cho0[i])
    x_min = x_min // k
    return x_min
def cho_att(x_min, n, k):
    count = k + 1
    x = x_min - 1
    while count >= k:
        x += 1
        if x == 0:
            x = 1
        count = 0
        for i in range(n):
            a = cho0[i][0] // x
            b = cho0[i][1] // x
            count += a * b
    return x - 1
n, k = map(int, input().split())
cho0 = []
for i in range(n):
    cho0.append(list(map(int, input().split())))
x_min = cho_minx(cho0, n, k)
x = cho_att(x_min, n, k)
print(x)