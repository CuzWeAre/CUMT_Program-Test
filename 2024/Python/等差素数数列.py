# 由计算机转专业群，24数学刘家蔚同学提供

def is_prime(n): #素数筛
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def loop_check(num,step,time): #本函数用于检测是否符合等差素数数列条件
    if time == 0: #base case
        return True
    if is_prime(num+step):  #递归
        return loop_check(num+step,step,time-1)
    return False

stop = 0 #状态值，0为继续，1为停止
for n in range(2,10000):
    if not is_prime(n):
        continue
    elif stop == 0:
        for step in range(2,10000): #枚举等差，逐个尝试
            if loop_check(n,step,8):
                print(step)
                stop = 1 #设置为停止
                break
    elif stop == 1:
        break