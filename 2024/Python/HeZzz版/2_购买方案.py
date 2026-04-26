"""
买礼物,输入礼物的价格(升序空格隔开),挑选其中三件,输出有多少种购买方式(组合)

例如:
输入
1 2 3 4 5

输出
10
"""

def calculate_combinations(n):
    """
    计算组合数 C(n, 3)
    """
    if n < 3:
        return 0
    if n == 3:
        return 1

    result = 1
    for i in range(1, 4):
        result *= (n - i + 1)
        result //= i

    return result

gift_prices = list(map(int, input().split()))
num = len(gift_prices)
print(calculate_combinations(num))