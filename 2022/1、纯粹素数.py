# 一个素数，去掉最高位，剩下的数仍为素数，再去掉剩下的数的最高位，余下的数还是素数。
def IsPrime(num: int) -> bool:
    """Check if num is prime"""
    if num <= 1:
        return False
    flag = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            flag = False
            break
    return flag


def IsPurePrime(num: int) -> bool:
    """Check if num is pure prime"""
    flag = True
    num = list(str(num))
    for i in range(len(num)):
        num_temp = num[i:]
        if not IsPrime(int("".join(num_temp))):
            flag = False
            break
    return flag


if __name__ == "__main__":
    num = int(input())
    ans_ispure = ["非纯粹素数", "为纯粹素数"][int(IsPurePrime(num))]
    if IsPrime(num):
        print(f"{num}是素数，且{ans_ispure}")
    else:
        print(f"{num}不是素数，且{ans_ispure}")
