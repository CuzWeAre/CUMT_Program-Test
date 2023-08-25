"""
十进制小数转换为二进制小数的方法：
将小数部分不断乘2，取整数部分作为二进制的一位。
将小数部分保留的小数部分再次乘2，取整数部分作为下一位二进制。
重复上述步骤，直到小数部分为0或者达到一定的精度。
"""


def decimal_to_binary(decimal, precision=8):
    binary = "0."

    for _ in range(precision):
        decimal *= 2
        digit = int(decimal)
        binary += str(digit)
        decimal -= digit

    return binary


decimal_number = 0.625
binary_representation = decimal_to_binary(decimal_number)
print(binary_representation)
