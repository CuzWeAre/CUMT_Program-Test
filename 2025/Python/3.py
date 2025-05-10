# 使用datetime库
import datetime
start = datetime.date(1921,7,23)
end = datetime.date(2020,7,1)
gap = end - start
print(gap.days*24*60)
