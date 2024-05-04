"""
测试数据：
10
John 20230002 88
Emily 20230003 92
Michael 20230004 78
Sophia 20230005 85
Jacob 20230006 94
Olivia 20230007 76
William 20230008 89
Ava 20230009 81
Ethan 20230010 70
Mia 20230011 96
"""

n = int(input())
data = [["Name", "ID", "Score"]]
student_info = [input().split(" ") for _ in range(n)]

# 按照成绩排序
student_info = sorted(student_info, key=lambda x: x[2], reverse=True)

# 计算每列的最大宽度
data += student_info
max_widths = [len(i) for i in data[0]]
for data_single in data[1:]:
    # max_widths = [len(data_single[i]) if len(data_single[i]) > max_widths[i] else max_widths[i] for i in range(len(data[0]))]
    for i in range(len(data[0])):
        if len(data_single[i]) > max_widths[i]:
            max_widths[i] = len(data_single[i])


# 打印表格
separation = (
    "|" + "|".join("-" * (max_widths[i] + 2) for i in range(len(data[0]))) + "|"
)
print(separation)
for data_single in data:
    print(
        "| "
        + " | ".join(f"{field:<{max_widths[i]}}" for i, field in enumerate(data_single))
        + " |"
    )
    print(separation)
