'''H数指满足4n+1(n∈N,n>=0)的数，例如1、5、9、13……
H素数是只能被1和本身整除的数，例如5、9、13……
H半素数是可以分解为两个H素数相乘的数，例如25、45、81、85……
求150以内的H半素数'''

import itertools

def ishprime(n:int) -> bool: #:int ->bool可以不写，说明性的代码
    '''判断是否为h素数'''
    if n <=1:
        return False
    
    #依赖于全局变量lst_h，需要在lst_h给出后再运行函数。实际上也可以改写函数名为ishprime(n:int,lst_h:list)，把lst_h作为参数传递进来
    for i in lst_h[1:]:#把1去了
        if n%i == 0 and n!=i:
            return False
    return True

lst_h = [4*n+1 for n in range(150) if 4*n+1<150] #range(150)是个随便的值，实际上只要4*n+1能取到最接近150的值范围任意
lst_hprime = [x for x in lst_h if ishprime(x)]
hprime_combinations = itertools.combinations(lst_hprime,2)#翘课了，这个库蛮好用的建议学。递归造轮子太折磨TAT
#print(list(hprime_combinations)) #去掉注释执行可观察返回的样子
#print(hprime_combinations) #和上面比较一下有什么不同
lst_halfprime = [[k[0]*k[1],k] for k in hprime_combinations if k[0]*k[1]<150]
lst_halfprime += [[k**2,(k,k)] for k in lst_hprime if k**2<150]#加上k**2排序方便
lst_halfprime.sort()
for i in lst_halfprime:
    print(f'{i[0]}={i[1][0]}*{i[1][1]}')