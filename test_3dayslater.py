import datetime
import calendar

# 大型連休のロジックを確認して追記したい

def threeWorkingDaysLater(n):
    marineday = get_day_of_nth_dow(n.year, 7, 3, 0)
    print(marineday)
    m = n + datetime.timedelta(days=3)
    # 土日の場合は2日すすめる
    if m.weekday() in [5, 6]:
        m = m + datetime.timedelta(days=2)
    # 海の日連休の場合は2日すすめる
    if m in [marineday, marineday+datetime.timedelta(days=1)]:
        m = m + datetime.timedelta(days=2)
    # GWの場合
    # お盆の場合
    # 年末年始の場合
    print('next working day is ****/**/**!')
    return m


def get_day_of_nth_dow(year, month, nth, dow):
    '''dow: Monday(0) - Sunday(6)'''
    if nth < 1 or dow < 0 or dow > 6 or month < 1 or month > 12:
        return None

    first_dow, n = calendar.monthrange(year, month)
    day = datetime.date(year, month, 7 * (nth - 1) + (dow - first_dow) % 7 + 1)

    return day

n = datetime.date(2021, 6, 17)
day = threeWorkingDaysLater(n)
print(day)