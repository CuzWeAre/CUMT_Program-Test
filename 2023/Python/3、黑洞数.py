'''读取一个四位不全相同的数字，这四个数字排列组合出最大的数和最小的数做差，之后重复这个步骤，最多7次数字最终便会变成 6174。
现在要求你编写程序，从键盘读入一个四位不全相同的数字，求需要像上面那样处理多少次掉入黑洞
例如1234这个数字只需要3次就会掉入黑洞
'''

N =list(input())
for i in range(1,8):
    #最多7次掉入黑洞
    N_min = int(''.join(sorted(N)))
    N_max = int(''.join(sorted(N,reverse=True)))
    N = N_max-N_min
    if N == 6174:
        print(i)
        break
    N = list(str(N))