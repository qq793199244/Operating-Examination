'''
输入任意年月日，输出是所属年的第几天
示例：
输入：
2021-9-9
输出：
252
'''


def func(year, month, day):
    count = 0
    # 闰年
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        list1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(month - 1):
            count += list1[i]
        return count + day
    # 平年
    else:
        list2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(month - 1):
            count += list2[i]
        return count + day


if __name__ == '__main__':
    s = str(input())
    s = s.split('-')
    year = int(s[0])
    month = int(s[1])
    day = int((s[2]))
    print(func(year, month, day))
