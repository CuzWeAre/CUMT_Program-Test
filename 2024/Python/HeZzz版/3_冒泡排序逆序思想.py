"""
小蓝最近学习了一些排序算法,其中冒泡排序让他印象深刻。在冒泡排序中,每次只能交换相邻的两个元素。小蓝发现,如果对一个字符串中的字符排序,只允许交换相邻的两个字符,则在所有可能的排序方案中,冒泡排序的总交换次数是最少的。
例如,对于字符串 lan 排序,只需要 1次交换。对于字符串 qiao 排序,总共需要 4 次交换。小蓝的幸运数字是 V,他想找到一个只包含小写英文字母的字符串,对这个串中的字符进行冒泡排序,正好需要 V 次交换。

请帮助小蓝找一个这样的字符串。如果可能找到多个,请告诉小蓝最短的那个。如果最短的仍然有多个,请告诉小蓝字典序最小的那个。请注意字符串中可以包含相同的字符。

输入格式
输入一行包含一个整数"V" ,为小蓝的幸运数字。
输出格式
输出一个字符串,为所求的答案。

样例输入
4

样例输出
bbaa

样例输入
100

样例输出
Jihgfeeddccbbaa
"""


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
    创建一个给定长度的字符串,按字母序排列(重复使用a-z）
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
