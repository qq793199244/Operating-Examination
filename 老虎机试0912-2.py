'''
题目
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（如180的质因子为2 2 3 3 5 ）
最后一个数后面也要有空格
输入描述
输入一个long型整数
输出描述
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。
'''


def func(n):
    for i in range(2, n + 1):
        if n % i == 0:
            print(str(i), end=' ')
            num = n // i
            func(num)
            break
    else:
        return


while True:
    try:
        n = int(input())
        func(n)
    except:
        break
