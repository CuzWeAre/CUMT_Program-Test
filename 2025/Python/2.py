# 明文加密(移位)
s = input()
l = int(input())

# 先根据长度分组
s = [s[i:i+l] for i in range(0, len(s), l)]

# 进行移位操作

for i in range(len(s)):
    d = i % len(s[i]) # 取余实现移位，防止爆索引。 如果没想到可以采取暴力拓宽字符串的方法。
    s[i] = s[i][-d:] + s[i][:-d] if d != 0 else s[i]
    
print(''.join(s))

