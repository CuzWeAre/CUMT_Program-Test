"""
求10~1000内满足条件的回文整数。

要求如下

（1）这个整数本身是回文数，假设该整数为i，则i的平方，i的立方也均为回文数。

（2）逐行输出这些符合条件的数字，并把其对应的平方，立方在同一行输出。

输出结果展示：


11 121 1331
101 10201 1030301
111 12321 1367631
"""


def is_palindrome(num_str):
    return num_str == num_str[::-1]


for i in range(10, 1000):
    if all(is_palindrome(str(x)) for x in (i, i ** 2, i ** 3)):
        print(f"{i} {i ** 2} {i ** 3}")
