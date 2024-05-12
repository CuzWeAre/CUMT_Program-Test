def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
diff = 0 # 公差
for i in range(2,1000):
    if not is_prime(i):
        continue
    else:
        for j in range(1,501):
            length = 0 # 记当前等差素数数列长度,同时每一次重新开始查找时重置为0
            for k in range(i + j,i + j * 11,j):
                if not is_prime(k):
                    break
                else:
                    length += 1
                if length == 9: # i是数列中第一个元素，我们检查时候是从i+j开始的
                    diff = j
                    break
print(diff)