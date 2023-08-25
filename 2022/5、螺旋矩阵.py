# https://leetcode.cn/problems/spiral-matrix-ii/


def generateMatrix(n: int):
    # 初始化矩阵
    matrix = [[0] * n for _ in range(n)]
    # 定义边界变量
    left, right, top, bottom = 0, n - 1, 0, n - 1
    # 定义要填充的元素值
    num = 1
    while left <= right and top <= bottom:
        # 填充上边界
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        # 填充右边界
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        # 填充下边界
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        # 填充左边界
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    return matrix


matrix = generateMatrix(4)
for row in matrix:
    row_str = " ".join(f"{num:>02}" for num in row)
    print(row_str)
