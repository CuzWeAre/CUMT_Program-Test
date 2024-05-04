import datetime

print("日期输入格式2022-01-01")
start = input("请输入起始时间：")
start_datetime = datetime.datetime.strptime(start, "%Y-%m-%d")
end = input("请输入截至时间：")
end_datetime = datetime.datetime.strptime(end, "%Y-%m-%d")

delta_datetime = end_datetime - start_datetime
days = delta_datetime.days
print(f"经过{days}天")

workdays = (days // 5) * 3
if days % 5 < 4:
    workdays += days % 5
else:
    workdays += 3
print(f"打渔{workdays}天，摸鱼{days-workdays}天")
