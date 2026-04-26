"""
儿童节那天有K位小朋友到小明家做客。小明拿出了珍藏的巧克力招待小朋友们。小明一共有N块巧克力,其中第i块是Hi x Wi的方格组成的长方形。为了公平起见,小明需要从这 N 块巧克力中切出K块巧克力分给小朋友们。切出的巧克力需要满足：
(1)形状是正方形,边长是整数
(2)大小相同
例如,一块6x5的巧克力可以切出6块2x2的巧克力,或者2块3x3的巧克力。
当然小朋友们都希望得到的巧克力尽可能大,你能帮小Hi计算出,最大的边长是多少么？

输入
第一行包含两个整数N和K。(1 <= N, K <= 100000)
以下N行每行包含两个整数Hi和Wi。(1 <= Hi, Wi <= 100000)
输入保证每位小朋友至少能获得一块1x1的巧克力。

输出
输出切出的正方形巧克力最大可能的边长。

运行示例
输入
2 10
6 5
5 6

输出
2
"""

class SolutionMethod1:
    """
    方法一: 通过遍历巧克力块,找到每块巧克力中最小边长的最大值,作为初始边长下界。
    然后通过二分查找找到能切出至少 k 个正方形的最大边长。
    """
    @staticmethod
    def cho_minx(cho0, n, k):
        """
        找到每块巧克力中最小边长的最大值,作为初始边长下界。

        参数:
        - cho0: 巧克力块的列表,每块巧克力用 [高度, 宽度] 表示。
        - n: 巧克力块的总数量。
        - k: 需要切出的正方形块数。

        返回:
        - x_min: 所有巧克力最小维度的最大值,除以 k。
        """
        x_min = 0

        for i in range(n):
            # 找到每块巧克力的最小边并更新 x_min
            if min(cho0[i]) > x_min:
                x_min = min(cho0[i])

        x_min = x_min // k  # 初始边长下界
        return x_min

    @staticmethod
    def cho_att(cho0, x_min, n, k):
        """
        找到能切出至少 k 个正方形的最大边长。

        参数:
        - cho0: 巧克力块的列表,每块巧克力用 [高度, 宽度] 表示。
        - x_min: 初始可能的最小边长。
        - n: 巧克力块的总数量。
        - k: 需要切出的正方形块数。

        返回:
        - 能切出至少 k 个正方形的最大边长。
        """
        count = k + 1  # 初始化一个大于 k 的 count 以进入循环
        x = x_min - 1  # 初始化 x,从 x_min-1 开始
        while count >= k:
            x += 1
            if x == 0:
                x = 1  # 确保 x 至少为 1
            count = 0
            for i in range(n):
                # 计算每块巧克力能切出的边长为 x 的正方形数量
                a = cho0[i][0] // x
                b = cho0[i][1] // x
                count += a * b
        return x - 1  # 返回找到的最大边长


class SolutionMethod2:
    """
    方法二: 使用二分查找来找到最大边长。
    通过检查每个可能的边长,判断是否可以从巧克力块中切出至少 k 个正方形。
    """
    @staticmethod
    def max_square_side(N, K, chocolates):
        """
        确定能从给定巧克力块中切出的最大正方形边长。

        参数:
        - N: 巧克力块的总数量。
        - K: 需要切出的正方形块数。
        - chocolates: 每个巧克力块的尺寸列表,每个元组表示 (高度, 宽度)。

        返回:
        - 可以切出的正方形的最大边长。
        """

        def can_cut_squares(side):
            """
            检查是否可以从巧克力块中切出至少 K 个边长为 side 的正方形。

            参数:
            - side: 正方形的边长。

            返回:
            - 如果可以切出至少 K 个正方形,返回 True；否则返回 False。
            """
            count = 0
            for h, w in chocolates:
                # 计算当前巧克力块可以切出的正方形数量
                count += (h // side) * (w // side)
                if count >= K:  # 提前退出,如果满足所需数量
                    return True
            return count >= K

        # 使用二分查找找到最大边长
        left, right = 1, min(max(h for h, w in chocolates), max(w for h, w in chocolates))
        while left <= right:
            mid = (left + right) // 2
            if can_cut_squares(mid):
                left = mid + 1  # 尝试更大的边长
            else:
                right = mid - 1  # 边长太大,尝试更小的边长

        return right


if __name__ == "__main__":
    # 输入部分
    N, K = map(int, input("输入巧克力数量和需要的正方形数量: ").split())
    chocolates = [list(map(int, input(f"输入第 {i+1} 块巧克力的尺寸 (高度 宽度): ").split())) for i in range(N)]

    # 解法1
    method1 = SolutionMethod1()
    x_min = method1.cho_minx(chocolates, N, K)
    result1 = method1.cho_att(chocolates, x_min, N, K)
    print(f"方法1: 能切出的最大正方形边长为 {result1}")

    # 解法2
    method2 = SolutionMethod2()
    result2 = method2.max_square_side(N, K, chocolates)
    print(f"方法2: 能切出的最大正方形边长为 {result2}")
