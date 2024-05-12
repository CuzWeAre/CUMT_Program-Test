def combinations_count(n):
    #计算组合数C(n,3)
    if n < 3:
        return 0
    if n == 3:
        return 1
    result = 1
    for i in range(1, 4):
        result *= (n - i + 1)
        result //= i
    return result
gift_prices = list(map(int,input().split()))
num = len(gift_prices)
print(combinations_count(num))