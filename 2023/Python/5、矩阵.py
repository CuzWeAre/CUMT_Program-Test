#比22年机考题简单，类似题目可看leetcode.cn 54,59题 关键词：螺旋矩阵
'''键盘读入一个正偶数n，生成一个(n-1)*(n-1)的矩阵，从外到里递增，即最里面的数是n/2。
例：输入10
1 1 1 1 1 1 1 1 1
1 2 2 2 2 2 2 2 1
1 2 3 3 3 3 3 2 1
1 2 3 4 4 4 3 2 1
1 2 3 4 5 4 3 2 1
1 2 3 4 4 4 3 2 1
1 2 3 3 3 3 3 2 1
1 2 2 2 2 2 2 2 1
1 1 1 1 1 1 1 1 1
'''

n = int(input())
matrix = [[0 for _ in range(n-1)] for _ in range(n-1)] #_代表不需用到迭代数具体值
for i in range(n-1):
    for up in range(i,n-1-i):
        matrix[i][up]=i+1
    for down in range(i,n-1-i):
        matrix[-i-1][down]=i+1
    for left in range(i,n-1-i):
        matrix[left][i]=i+1
    for right in range(i,n-1-i):
        matrix[right][-i-1]=i+1
        
for x in matrix:
    x = map(str,x)
    print(' '.join(x))
        
    #可以把上面的循环注释掉，下面的代码去掉注释，以便于观察每次操作后矩阵的变化
    # for x in matrix:
    #     x = map(str,x)
    #     print(' '.join(x))
    
    # print()