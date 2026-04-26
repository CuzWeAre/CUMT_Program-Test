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
                    break  # 只要有一个不是素数,立即停止检查

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


# TODO: 根据素数筛生成素数列表, 以提高效率


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