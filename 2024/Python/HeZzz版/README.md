# 2024 年 Python 机考题目及解答

**作者：** [HeZzz](https://github.com/HeZ2z)

**日期：** 2024-05-06

---

- [2024 年 Python 机考题目及解答](#2024-年-python-机考题目及解答)
  - [第一题：回文数字](#第一题回文数字)
  - [第二题：购买方案（组合）](#第二题购买方案组合)
  - [第三题：冒泡排序逆序思想](#第三题冒泡排序逆序思想)
  - [第四题：巧克力](#第四题巧克力)
  - [第五题：等差素数数列](#第五题等差素数数列)

---

## [第一题：回文数字](1_回文数字.py)

**题目描述：**
求 10\~1000 范围内，满足下列条件的回文整数：

1. 整数本身是回文数。
2. 该整数的平方与立方也均为回文数。
   逐行输出这些符合条件的数字，并在同一行输出其对应的平方和立方。

**输出示例：**

```text
11 121 1331
101 10201 1030301
111 12321 1367631
```

**思考：**
此题考查字符串回文判断与简单循环遍历的综合运用，思路直观，直接将整数及其平方、立方转为字符串后判断即可。

**题解：**

```python
def is_palindrome(num_str):
    """判断一个字符串是否是回文数,非常常见题型,随便写一个能过的就好"""
    return num_str == num_str[::-1]


for i in range(10, 1000):
    if all(is_palindrome(str(x)) for x in (i, i ** 2, i ** 3)):
        print(f"{i} {i ** 2} {i ** 3}")
```

---

## [第二题：购买方案（组合）](2_购买方案.py)

**题目描述：**
输入若干礼物的价格（升序、空格分隔），从中任选三件，问共有多少种购买方式（组合数）。

**输入示例：**

```text
1 2 3 4 5
```

**输出示例：**

```text
10
```

**思考：**
本题仅需计算 C(n, 3)，其中 n 为礼物数量。可用组合数公式直接计算，无需列举具体三元组。

**题解：**

```python
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
```

---

## [第三题：冒泡排序逆序思想](3_冒泡排序逆序思想.py)

**题目描述：**
对字符串中的字符进行排序，只允许交换相邻字符。证明冒泡排序方案的交换次数最少。
给定幸运数字 V，找一个只包含小写字母的字符串，使对其进行冒泡排序恰好需要 V 次交换。

* 若存在多个，输出最短的；
* 最短仍有多解，则输出字典序最小的；
* 字符串中可包含相同字符。

**样例 1：**
输入：

```text
4
```

输出：

```text
bbaa
```

**样例 2：**
输入：

```text
100
```

输出：

```text
Jihgfeeddccbbaa
```

**思考：**

关键在于将交换次数与字符串的逆序对数对应，接着通过构造基本序列与“多余”逆序对插入的方法，满足最小长度和字典序要求。

其中根据 V 计算所需字符串的最小长度，使用 `length(v)` 函数。因为对于长度为 n 的字符串，最多有 n(n-1)/2 个逆序对。所以，给定 V，最小长度 n 满足 n(n-1)/2 >= V。

然后根据最小长度 n，计算出多余的逆序对数 `add_number`，即 `add_number = n(n-1)/2 - V`。

接着创建一个基本字符串 `base_string`，长度为 n - add_number，按字母序排列。最后在基本字符串中插入字符，使得逆序对数符合要求。

**题解：**

```python
def length(v):
    """
    根据V计算所需字符串的最小长度
    """
    i = 1
    while i * (i - 1) // 2 < v:
        i += 1
    return i


def create_string(length):
    """
    创建一个给定长度的字符串,按字母序排列(重复使用a-z)
    """
    base_ord = ord('a')
    return ''.join(chr(base_ord + i % 26) for i in range(length))


def add_chars(add_number, base_string):
    """
    在基本字符串中插入字符,使得逆序对数符合要求
    """
    # 将基本字符串转换为列表以进行插入操作
    result = list(base_string)
    alpha_ord = ord('a')
    index = 0

    # 插入字符
    for _ in range(add_number):
        result.insert(index + 1, chr(alpha_ord))
        index += 2
        alpha_ord = (alpha_ord - ord('a') + 1) % 26 + ord('a')

    # 返回逆序排序的字符串
    return ''.join(sorted(result, reverse=True))


if __name__ == "__main__":
    V = int(input("请输入幸运数字：").strip())

    # 计算最小长度及多余字符的数量
    len_needed = length(V)
    add_chars_needed = len_needed * (len_needed - 1) // 2 - V

    # 创建基本字符串并插入多余字符
    base_string = create_string(len_needed - add_chars_needed)
    result_string = add_chars(add_chars_needed, base_string)

    print(result_string)
```

---

## [第四题：巧克力](4_巧克力.py)

**题目描述：**
儿童节有 K 位小朋友来访，小明有 N 块巧克力，第 i 块尺寸为 Hi×Wi。
需要切出 K 块同尺寸的整数边长正方形，且最大化边长。
输出最大可能的边长。

**输入格式：**

```
N K
H₁ W₁
H₂ W₂
…
Hₙ Wₙ
```

**示例：**

```
2 10
6 5
5 6
```

输出：

```
2
```

**思考：**

典型“在答案范围上二分”的应用。只需对每个候选边长统计总块数，判断是否≥K，并调整二分区间即可。

方法一：遍历巧克力块，找到每块巧克力中最小边长的最大值，作为初始边长下界。然后通过二分查找找到能切出至少 K 个正方形的最大边长。

方法二：使用二分查找来找到最大边长。通过检查每个可能的边长，判断是否可以从巧克力块中切出至少 K 个正方形。

**题解：**

```python
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
```

---

## [第五题：等差素数数列](5_等差素数数列.py)

**题目描述：**
已知质数序列 2,3,5,7,11,13。若完全由质数组成的等差数列（公差相同）且长度为 6 的例子有

```
7, 37, 67, 97, 127, 157
```

Green–Tao 定理保证存在任意长度的等差素数序列。请搜索长度为 10 的等差素数序列，其最小公差是多少？

**思考：**
暴力方法效率极低，需要借助数论性质或预先筛出质数来加速搜索。本题可分别尝试枚举、公差递增、及利用质数乘积构造公差等多种策略。

法一二不多赘述，思路很简单。

法三主要运用了 **模余约束**，将公差设计为若干小素数的乘积，如果公差是 2*3*5*7 = 210，那么我们可以得到 210, 420, 630, ... 这些数都是等差数列的公差。

从而我们可以通过 `generate_primes` 函数来生成所有小于 limit 的素数列表，然后通过 `find_arithmetic_prime_sequence` 函数来找到长度为 arr_length 的等差素数数列及其公差。

当然，法三的实现也可以使用其他方法来生成素数列表，比如各种筛法，同学们感兴趣的话可以自己实现。

**题解：**

```python
import math

def is_prime(n):
    """判断一个数是否是素数"""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

class SolutionBase:
    """所有解法类的基类,包含常用的方法"""

    @staticmethod
    def is_prime(n):
        """判断一个数是否是素数"""
        return is_prime(n)

    def find_next_prime(self, n):
        """找到比 n 大的下一个素数"""
        n += 1
        while not self.is_prime(n):
            n += 1
        return n

class SolutionMethod1(SolutionBase):
    """方法一：暴力枚举法"""

    def arr_diff_equal(self, arr):
        """
        判断一个数组的差值是否相等(即是否为等差数列)

        参数:
        - arr: 素数序列数组

        返回:
        - 布尔值,表示数组是否为等差数列
        """
        if len(arr) < 2:
            return True
        diff = arr[1] - arr[0]
        return all(arr[i] - arr[i - 1] == diff for i in range(1, len(arr)))

    def find_diff_prime(self, arr_length):
        """
        找到一个长度为 arr_length 的等差素数数列

        参数:
        - arr_length: 等差数列的长度

        返回:
        - 公差和等差素数数列
        """
        i = 2
        while True:
            prime_arr = []
            diff = self.find_next_prime(i) - i
            for j in range(arr_length):
                candidate = i + j * diff
                if self.is_prime(candidate):
                    prime_arr.append(candidate)
                else:
                    break
            if len(prime_arr) == arr_length and self.arr_diff_equal(prime_arr):
                return diff, prime_arr
            i = self.find_next_prime(i)

class SolutionMethod2(SolutionBase):
    """
    方法二：递归检查法 (由转计算机交流群, 24数学刘家蔚同学提供)
    """ 

    def loop_check(self, num, step, arr_length):
        """
        递归检查是否可以形成长度为 arr_length 的等差素数数列

        参数:
        - num: 等差数列的起始素数
        - step: 等差数列的公差
        - arr_length: 需要的素数数列长度

        返回:
        - 布尔值,表示是否可以形成等差素数数列
        """
        if arr_length == 0:
            return True
        return self.is_prime(num + step) and self.loop_check(num + step, step, arr_length - 1)

    def find_out(self, arr_length):
        """
        找到长度为 arr_length 的等差素数数列的最小公差

        参数:
        - arr_length: 等差数列的长度

        返回:
        - 公差
        """
        for n in range(2, 10000):
            if not self.is_prime(n):
                continue
            for step in range(2, 10000):
                if self.loop_check(n, step, arr_length):
                    return step

class SolutionMethod3(SolutionBase):
    """方法三：利用等差数列的性质优化解法"""

    def generate_primes(self, limit):
        """
        生成所有小于 limit 的素数列表

        参数:
        - limit: 最大范围

        返回:
        - 素数列表
        """
        return [num for num in range(2, limit) if self.is_prime(num)]

    def find_arithmetic_prime_sequence(self, arr_length):
        """
        找到长度为 arr_length 的等差素数数列及其公差

        参数:
        - arr_length: 等差数列的长度

        返回:
        - 公差和等差素数数列
        """
        primes = self.generate_primes(arr_length)
        step = 1
        for prime in primes:
            step *= prime  # 用素数的乘积作为公差

        start = 2
        while True:
            sequence = [start + i * step for i in range(arr_length)]
            if all(self.is_prime(num) for num in sequence):
                return step, sequence
            start = self.find_next_prime(start)

def main():
    arr_length = int(input("请输入等差数列的长度："))
    print("请选择算法方法：")
    print("1. 方法一：暴力枚举")
    print("2. 方法二：递归检查")
    print("3. 方法三：等差数列的性质")

    choice = input("请输入选择(1/2/3)：")

    if choice == '1':
        sm1 = SolutionMethod1()
        diff, prime_arr = sm1.find_diff_prime(arr_length)
        print(f"方法1 - 公差为：{diff}")
        print(f"等差素数数列为：{prime_arr}")
    elif choice == '2':
        sm2 = SolutionMethod2()
        print(f"方法2 - 公差为：{sm2.find_out(arr_length)}")
    elif choice == '3':
        sm3 = SolutionMethod3()
        diff, prime_sequence = sm3.find_arithmetic_prime_sequence(arr_length)
        print(f"方法3 - 公差为：{diff}")
        print(f"等差素数数列为：{prime_sequence}")
    else:
        print("无效的选择,请重新运行程序并选择 1, 2 或 3")

if __name__ == '__main__':
    main()

```
