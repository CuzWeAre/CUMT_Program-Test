'''回文日期指的是一个日期表示为yyyymmdd的形式后，yyyymmdd是个回文数。例如20200202是一个回文日期，它的下一个回文日期是20211202。
给定一个yyyymmdd的日期，求下一个回文日期是在哪一天。'''

#ChatGpt提供的答案
#鼠鼠我啊，机考没做出来，疯狂造轮子，考得是一点不会(Ｔ▽Ｔ)
from datetime import datetime, timedelta

def is_palindrome(num):
    """判断给定的整数是否为回文数"""
    str_num = str(num)
    return str_num == str_num[::-1]

def next_palindrome_date(date):
    """计算给定日期的下一个回文日期"""
    curr_date = datetime.strptime(date, "%Y%m%d")
    # 逐个增加日期，直到找到回文日期为止
    while True:
        curr_date += timedelta(days=1)
        next_date_str = datetime.strftime(curr_date, "%Y%m%d")
        if is_palindrome(int(next_date_str)):
            return next_date_str

date_str = input()#"输入一个日期（格式为YYYYMMDD）
datetime.strptime(date_str, "%Y%m%d")
next_palindrome = next_palindrome_date(date_str)
print(next_palindrome)


#不用库的版本
def is_palindrome(num):
    """判断给定的整数是否为回文数"""
    str_num = str(num)
    return str_num == str_num[::-1]

def is_valid_date(date):
    """判断给定的日期是否合法"""
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
    if year < 1000 or year > 9999 or month < 1 or month > 12:
        return False
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return day >= 1 and day <= 31
    elif month in {4, 6, 9, 11}:
        return day >= 1 and day <= 30
    elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return day >= 1 and day <= 29
    else:
        return day >= 1 and day <= 28

def next_palindrome_date(date):
    """计算给定日期的下一个回文日期"""
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
    while True:
        # 逐个增加日期
        day += 1
        if day > 31 or (day > 30 and month in {4, 6, 9, 11}) or (day > 29 and month == 2) or (day > 28 and month == 2 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))):
            day = 1
            month += 1
        if month > 12:
            month = 1
            year += 1
        # 构造下一个日期并判断是否为回文日期
        next_date = f"{year:04d}{month:02d}{day:02d}"
        if is_valid_date(next_date) and is_palindrome(next_date):
            return next_date
