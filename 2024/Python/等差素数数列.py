"""
2,3,5,7,11,13.是素数序列。
类似我1们有:7，37，67，97，127，157这样完全由素数组成的等差数列，叫等差素数数列，
而这个等差素数数列的公差为30，长度为6。
2004年，格林与华人陶哲轩合作证明了:存在任意长度的素数等差数列。这是数论领域一项惊人的成果!
有这一理论为基础，请你借助手中的计算机，满怀信心地搜索长度为10的等差素数列，其公差最小值是多少?
"""


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
    """所有解法类的基类，包含常用的方法"""

    @staticmethod
    def is_prime(n):
        return is_prime(n)

    def find_next_prime(self, n):
        """找到比 n 大的下一个素数"""
        n += 1
        while not self.is_prime(n):
            n += 1
        return n


class SolutionMethod1(SolutionBase):
    """方法一：暴力枚举"""

    def arr_diff_equal(self, arr):
        """判断一个数组的差值是否相等"""
        if len(arr) < 2:
            return True
        diff = arr[1] - arr[0]
        return all(arr[i] - arr[i - 1] == diff for i in range(1, len(arr)))

    def find_diff_prime(self, arr_length):
        """找到一个长度为 arr_length 的等差素数数列"""
        i = 2
        while True:
            prime_arr = []
            diff = self.find_next_prime(i) - i
            for j in range(arr_length):
                candidate = i + j * diff
                if self.is_prime(candidate):
                    prime_arr.append(candidate)

            if len(prime_arr) == arr_length and self.arr_diff_equal(prime_arr):
                return diff, prime_arr
            i = self.find_next_prime(i)


class SolutionMethod2(SolutionBase):
    """
    方法二：递归检查
    由计算机转专业群，24数学刘家蔚同学提供
    """

    def loop_check(self, num, step, arr_length):
        """递归检查等差数列是否为素数"""
        if arr_length == 0:
            return True
        return self.is_prime(num + step) and self.loop_check(num + step, step, arr_length - 1)

    def find_out(self, arr_length):
        """找到等差数列的公差"""
        for n in range(2, 10000):
            if not self.is_prime(n):
                continue
            for step in range(2, 10000):
                if self.loop_check(n, step, arr_length):
                    return step


class SolutionMethod3(SolutionBase):
    """方法三：利用等差数列的性质优化解法"""

    def generate_primes(self, limit):
        """生成所有小于 limit 的素数列表"""
        return [num for num in range(2, limit) if self.is_prime(num)]

    def find_arithmetic_prime_sequence(self, arr_length):
        """找到长度为 arr_length 的等差素数数列及其公差"""
        primes = self.generate_primes(arr_length)
        step = 1
        for prime in primes:
            step *= prime

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

    choice = input("请输入选择（1/2/3）：")

    if choice == '1':
        sm1 = SolutionMethod1()
        diff, prime_arr = sm1.find_diff_prime(arr_length)
        print(f"公差为：{diff}")
        print(f"等差素数数列为：{prime_arr}")
    elif choice == '2':
        sm2 = SolutionMethod2()
        print(f"公差为：{sm2.find_out(arr_length)}")
    elif choice == '3':
        sm3 = SolutionMethod3()
        diff, prime_sequence = sm3.find_arithmetic_prime_sequence(arr_length)
        print(f"公差为：{diff}")
        print(f"等差素数数列为：{prime_sequence}")
    else:
        print("无效的选择，请重新运行程序并选择 1, 2 或 3")


if __name__ == '__main__':
    main()
